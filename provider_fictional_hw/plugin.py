from __future__ import annotations

from provider_fictional_hw import __version__
from variantlib.models.provider import ProviderConfig
from variantlib.models.provider import VariantFeatureConfig


class FictionalHWPlugin:
    __provider_name__ = "fictional_hw"
    __version__ = __version__

    def _get_supported_architectures(self) -> list[str]:
        """Lookup the system to decide what `architecture` are supported on this system.
        Returns a list of strings in order of priority."""
        return ["deepthought", "HAL9000"]

    def _get_supported_compute_capability(self) -> list[str]:
        """Lookup the system to decide what `compute_capability` are supported on this
        system.
        Returns a list of strings in order of priority."""
        return ["10", "6", "2"]

    def _get_supported_compute_accuracy(self) -> list[str]:
        """Lookup the system to decide what `compute_accuracy` are supported on this
        system.
        Returns a list of strings in order of priority."""
        return ["1000", "0", "10"]

    def _get_supported_humor(self):
        """Lookup the system to decide what `humor` are supported on this system.
        Returns a list of strings in order of priority."""
        return ["0", "2"]

    def get_supported_configs(self) -> ProviderConfig:
        keyconfigs = []

        # Top Priority
        if (values := self._get_supported_architectures()) is not None:
            keyconfigs.append(VariantFeatureConfig(name="architecture", values=values))

        # Second Priority
        if (values := self._get_supported_compute_capability()) is not None:
            keyconfigs.append(
                VariantFeatureConfig(name="compute_capability", values=values)
            )

        # Third Priority
        if (values := self._get_supported_humor()) is not None:
            keyconfigs.append(VariantFeatureConfig(name="humor", values=values))

        # Fourth Priority
        if (values := self._get_supported_compute_accuracy()) is not None:
            keyconfigs.append(
                VariantFeatureConfig(name="compute_accuracy", values=values)
            )

        if keyconfigs:
            return ProviderConfig(
                provider=FictionalHWPlugin.__provider_name__,
                configs=keyconfigs,
            )

        return None
