"""# Amphibian.

AmphibianData class and associated methods. Used to represent the amphibian
data from the dataset/database to insert into the create pdf process.

"""


class AmphibianData:
    """AmphibianData.

    Class Representing the data scraped from the data source with additional
    helper methods

    Args:
        amp_info: list passed to init

    """

    def __init__(self, amp_info: list) -> None:
        """Init method for Amphibian Data.

        Instantiates AmphibianData class.

        Args:
            amp_info: amphibian info list

        """
        self.position = self.rtz(amp_info[0])
        self.order = self.rtz(amp_info[1])
        self.family = self.rtz(amp_info[2])
        self.genus = self.rtz(amp_info[3])
        self.species = self.rtz(amp_info[4])
        self.body_size_max = self.get_SVLMx(amp_info)
        self.longevity = self.rtz(amp_info[8])
        self.nesting_site = self.rtz(amp_info[9])
        self.clutch = self.get_clutch(amp_info)
        self.parity_mode = self.rtz(amp_info[13])
        self.egg_diameter = self.rtz(amp_info[14])
        self.activity = self.rtz(amp_info[15])
        self.microhabitat = self.rtz(amp_info[16])
        self.IUCN_category = self.rtz(amp_info[18])
        self.population_trend = self.rtz(amp_info[19])
        self.range_size = self.rtz(amp_info[20])
        self.elevation = self.get_elevation(amp_info)
        self.image_url_male = ""
        self.image_url_female = ""
        self.geographic_region = self.get_geographic_regions(amp_info)

        # fecundity, egg hatching, age maturity, metamorphosis are missing

    def get_geographic_regions(self, amp_info: list) -> str:
        geo = amp_info[17]
        geo = geo.split(",")
        geo_n = []
        for g in geo:
            a = g.replace("Nocontinent", "")
            a = a.replace(" Nocountry", "")
            a = a.replace("Noregion", "")
            a = a.strip("/")
            geo_n.append(a)
        geo_set = {x for x in geo_n}
        geo_l = [*geo_set]
        return "/".join(geo_l)

    def get_SVLMx(self, amp_info: list) -> str:
        """Get SVLMx."""
        SVLMx = f"Male: {self.rtz(amp_info[5])}"
        SVLMx += f"{' ' * (10 - len('male: ' + str(self.rtz(amp_info[5]))))}| "
        SVLMx += f"Female: {self.rtz(amp_info[6])}{' ' * (10 - len('Female: ' + str(self.rtz(amp_info[6]))))}|"
        SVLMx += f" Average: {self.rtz(amp_info[7])}"

        return SVLMx

    def get_clutch(self, amp_info: list) -> str:
        """Get Clutch."""
        clutch = f"Min: {self.rtz(amp_info[10])}{' ' * (10 - len('min: ' + str(amp_info[10])))}| "
        clutch += f"Max: {self.rtz(amp_info[11])}{' ' * (10 - len('max: ' + str(self.rtz(amp_info[11]))))}| "
        clutch += f"Average: {self.rtz(amp_info[12])}"

        return clutch

    def get_elevation(self, amp_info: list) -> str:
        """Get Elevation."""
        elevation = f"Min: {self.rtz(amp_info[21])}{' ' * (10 - len('min: ' + str(self.rtz(amp_info[21]))))}| "
        elevation += f"Max: {self.rtz(amp_info[22])}{' ' * (10 - len('max: ' + str(self.rtz(amp_info[22]))))}| "
        elevation += f"Average: {self.rtz(amp_info[23])}"

        return elevation

    def get_full_name(self) -> str:
        """Get full name.

        Returns the string of the combination of the Amphibian Object's order
        family genus and species

        Return:
            full_name(str)

        """
        return f"{self.order} {self.family} {self.genus} {self.species}"

    def get_short_name(self) -> str:
        """Get short name.

        Returns the string of the combination of the Amphibian Object's genus and
        species

        Return:
            short_name(str)

        """
        return f"{self.genus} {self.species}"

    def get_image_url(self) -> str:
        """Get image url.

        Returns the string of the image url

        Currently unimplemented
        """
        return ""

    def has_image_url(self) -> bool:
        """Check if class has image url.

        Returns boolean value based on the contents of the image_url_male
        and image_url_female properties

        Return:
            bool
        """
        return self.image_url_male != "" and self.image_url_female != ""

    def rtz(self, val) -> str:
        """Remove trailing zero"""
        if val != "Unknown":
            try:
                if float(val) % 1 == 0:
                    val = int(val)
                else:
                    val = f"{val:.2f}"
            except:
                pass
        else:
            val = "Unavailable"
        return val
