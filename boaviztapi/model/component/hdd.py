import boaviztapi.utils.roundit as rd
from boaviztapi.model.boattribute import Boattribute
from boaviztapi.model.component.component import Component, ComputedImpacts


class ComponentHDD(Component):
    NAME = "HDD"

    __DISK_TYPE = 'hdd'

    DEFAULT_HDD_CAPACITY = 500

    IMPACT_FACTOR = {
        'gwp': {
            'impact': 31.10
        },
        'pe': {
            'impact': 276.00
        },
        'adp': {
            'impact': 2.50E-04
        }
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.capacity = Boattribute(unit="GB", default=self.DEFAULT_HDD_CAPACITY)

    def impact_manufacture_gwp(self) -> ComputedImpacts:
        return self.__impact_manufacture('gwp')

    def __impact_manufacture(self, impact_type: str) -> ComputedImpacts:
        impact = self.IMPACT_FACTOR[impact_type]['impact']
        significant_figures = rd.min_significant_figures(impact)
        return impact, significant_figures, 0, []

    def impact_manufacture_pe(self) -> ComputedImpacts:
        return self.__impact_manufacture('pe')

    def impact_manufacture_adp(self) -> ComputedImpacts:
        return self.__impact_manufacture('adp')