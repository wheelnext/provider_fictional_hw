from variantlib.config import KeyConfig
from variantlib.config import ProviderConfig

from provider_fictional_hw import __version__


class FictionalHWPlugin:
    __provider_name__ = "fictional_hw"
    __version__ = __version__

    def _get_supported_architectures(self) -> list[str]:
        """Lookup the system to decide what `architecture` are supported on this system.
        Returns a list of strings in order of priority."""
        return ["HAL9000", "tars", "mother"]

    def _get_supported_compute_capability(self) -> list[str]:
        """Lookup the system to decide what `compute_capability` are supported on this
        system.
        Returns a list of strings in order of priority."""
        return ["8", "2", "0"]

    def _get_supported_compute_accuracy(self) -> list[str]:
        """Lookup the system to decide what `compute_accuracy` are supported on this
        system.
        Returns a list of strings in order of priority."""
        return ["1000000000", "100000", "25"]

    def _get_supported_humor(self):
        """Lookup the system to decide what `humor` are supported on this system.
        Returns a list of strings in order of priority."""
        return ["15", "1", "6"]

    def run(self) -> ProviderConfig:
        keyconfigs = []

        # Top Priority
        if (values := self._get_supported_architectures()) is not None:
            keyconfigs.append(KeyConfig(key="architecture", values=values))

        # Second Priority
        if (values := self._get_supported_compute_capability()) is not None:
            keyconfigs.append(KeyConfig(key="compute_capability", values=values))

        # Third Priority
        if (values := self._get_supported_humor()) is not None:
            keyconfigs.append(KeyConfig(key="humor", values=values))

        # Fourth Priority
        if (values := self._get_supported_compute_accuracy()) is not None:
            keyconfigs.append(KeyConfig(key="compute_accuracy", values=values))

        if keyconfigs:
            return ProviderConfig(
                provider=FictionalHWPlugin.__provider_name__,
                configs=keyconfigs,
            )

        return None
