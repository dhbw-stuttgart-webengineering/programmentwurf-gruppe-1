"""Semester class for the dualis module"""

import logging
import re

import bs4

from .dualis_session import DualisSession
from .module import Module
from .unit import Unit

logger = logging.getLogger(__name__)


class WebScraper:
    """Represents a semester in the dualis system
    """

    HTTP_DHBW = 'https://dualis.dhbw.de/scripts/mgrqispi.dll?'

    def __init__(self, session: DualisSession) -> None:
        self.session = session

    def scrape(self) -> list[Module]:
        """Scrapes all modules and units from the dualis system

        Returns:
            list[Module]: List of Modules
        """

        all_modules = []

        for semester in self._scrape_semester_dropdown():
            modules = [Module(*args)
                       for args in self._scrape_modules(*semester)]
            for module in modules:
                module.units = [Unit(
                    **args) for args in self._scrape_units(module.module_detail_link)]
                for unit in module.units:
                    unit.set_credit_points(
                        module.get_credits() / len(module.units))

            all_modules.extend(modules)
        return all_modules

    def scrape_username(self) -> str:
        """Returns the name of the user

        Returns:
            str: Name of the user
        """
        soup = self.session.get(
            self.HTTP_DHBW +
            "APPNAME=CampusNet&PRGNAME=MLSSTART&" +
            f"ARGUMENTS=-N{self.session.get_authtoken()},-N000019,")

        name_pattern = r'Herzlich willkommen, (.*?)!'

        match = re.search(name_pattern, soup.find("h1").text.strip())

        if match:
            return match.group(1)

    def _scrape_semester_dropdown(self) -> list:
        """Returns a list of semester objects

        Returns:
            list: List of semester objects
        """
        soup = self.session.get(
            self.HTTP_DHBW + "APPNAME=CampusNet&PRGNAME=COURSERESULTS&" +
            f"ARGUMENTS=-N{self.session.get_authtoken()},-N000307,")

        return [(option.text, option["value"]) for option in soup.find_all("option")]

    def _scrape_modules(self, semester_name: str, semester_link: str) -> list:
        modules = []

        soup = self.session.get(
            self.HTTP_DHBW + "APPNAME=CampusNet&PRGNAME=COURSERESULTS" +
            f"&ARGUMENTS=-N{self.session.get_authtoken()}" +
            f",-N000307,-N{semester_link},")

        table = soup.find("table", {"class": "nb list"})

        for semester_row in table.find_all("tr"):
            try:
                regex = r'\,-N([\d]*)\",\"'
                regex_name = r'^([^\(]*)'

                id_ = semester_row.find_all("td", {"class": "tbdata"})[
                    0].text.strip()
                name = re.search(regex_name, semester_row.find_all("td", {"class": "tbdata"})[
                    1].text.strip()).group(1).strip()
                credits_ = float(semester_row.find_all("td", {"class": "tbdata_numeric"})[
                    1].text.strip().replace(",", "."))
                module_detail_link = re.search(regex, semester_row.find_all(
                    "td", {"class": "tbdata"})[3].find("script").text).group(1)

                modules.append((id_,
                                name,
                                semester_name,
                                module_detail_link,
                                credits_,))

            except IndexError:
                continue
        return modules

    def _scrape_units(self, module_detail_link: str) -> list:

        unit_soup = self.session.get(
            self.HTTP_DHBW +
            f"APPNAME=CampusNet&PRGNAME=RESULTDETAILS&ARGUMENTS=-N{self.session.get_authtoken()}" +
            f",-N000307,-N{module_detail_link},")

        return self._extract_unit_info(unit_soup)

    def _extract_unit_info(self, soup: bs4.BeautifulSoup) -> list:
        units = {}
        table = soup.find("table", {"class": "tb"})

        last_header = None
        for row in table.find_all("tr"):
            columns = row.find_all("td")

            # Row with colspan=8 contains the unit name and id
            if columns[0].has_attr('colspan') is True and columns[0]['colspan'] == "8":

                # True, when one unit is in the module. Uses page heading as module name.
                if "Modulabschlussleistungen" in columns[0].text:
                    header = soup.find("h1").text.strip()
                else:  # Module has multiple units
                    header = columns[0].text.strip()

                if header not in units.keys():
                    unit_id, unit_name = self._extract_name_and_id(header)
                    units[header] = {"id_": unit_id,
                                     "name": unit_name}
                last_header = header

            elif columns[0].has_attr('class') and 'tbdata' in columns[0]['class']:
                grade = (float(columns[3].text.strip().replace(",", "."))
                         if "noch nicht gesetzt" not in columns[3].text else None)

                if "grade_first_attempt" in units[last_header].keys():
                    units[last_header]["grade_second_attempt"] = grade
                else:
                    units[last_header]["grade_first_attempt"] = grade

        return units.values()

    def _extract_name_and_id(self, module: str) -> (str, str):

        # Adjust for NBSP and split
        pattern = r'^([\S]{9}(?:.1)*)(?: |[\S\s]{3})([^\n]*) \([\s\S]{9,12}\)'

        match = re.search(pattern=pattern, string=module)
        return match.group(1), match.group(2)
