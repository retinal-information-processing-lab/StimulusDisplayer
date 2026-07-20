"""Display settings of each rig, for the standalone Stimulus Displayer.

This is the small subset of the rig hardware description that reading a stimulus ".bin"
needs. It mirrors the "display" fields of ``params.rig_params`` in the Standard analysis
pipeline, which is the reference: if a rig is added or corrected there, copy the change
here (and keep ``binfile.py`` identical between the two repositories).

Per rig:
    max_frame_size     largest image the rig can display [x, y] in pixels, or None for
                       no size check (rig not characterised yet)
    invert_polarity    True if the rig displays inverted, so frames are stored inverted
                       and must be flipped back (value -> 1 - value) when read
    optical_transform  geometric correction for this rig's optical path, applied when
                       reading/writing a .bin: "rot90_flipud", "fliplr", or None

Only MEA 2 and 3 are implemented AND tested. The others are WORK IN PROGRESS: they are
allowed (so you can still look at a file), but anything left as None falls back to a
neutral default — no optical correction, no polarity inversion, no size check — so the
frames may come out mirrored, rotated or inverted. Only rely on them if you know what
you are doing.
"""

RIG_SETTINGS = {
    1: {
        "max_frame_size": None,
        "invert_polarity": None,
        "optical_transform": None,
    },
    2: {
        "max_frame_size": [1920, 1080],
        "invert_polarity": False,
        "optical_transform": "rot90_flipud",
    },
    3: {
        "max_frame_size": [1024, 768],
        "invert_polarity": True,
        "optical_transform": "fliplr",
    },
    4: {
        "max_frame_size": None,
        "invert_polarity": None,
        "optical_transform": None,
    },
    5: {
        "max_frame_size": None,
        "invert_polarity": None,
        "optical_transform": "rot90_flipud",
    },
}

# Rigs whose display settings are implemented and tested.
DISPLAY_READY_RIGS = (2, 3)


def get_rig_settings(mea: int) -> dict:
    """Display settings of one rig, ready to pass to ``BinFile(..., rig_settings=...)``.

    Warns for a rig that is not implemented/tested yet, then falls back to neutral
    defaults for whatever it does not define, instead of blocking you.
    """
    import warnings

    if mea not in RIG_SETTINGS:
        raise ValueError(
            f"MEA {mea} is not defined in rig_settings.py (known rigs: {sorted(RIG_SETTINGS)}). "
            "Add its settings there, mirroring params.rig_params in the analysis pipeline."
        )
    settings = RIG_SETTINGS[mea]
    if mea not in DISPLAY_READY_RIGS:
        missing = [k for k, v in settings.items() if v is None]
        warnings.warn(
            f"MEA {mea}: reading/writing stimulus .bin files is WORK IN PROGRESS — this rig has "
            f"not been implemented or tested (tested rigs: {list(DISPLAY_READY_RIGS)}).\n"
            f"  Settings not defined for it: {missing or 'none'}.\n"
            "  Falling back to neutral defaults for those: no optical correction, no polarity "
            "inversion, no frame-size check.\n"
            "  The frames you read/write may therefore be mirrored, rotated or inverted.",
            stacklevel=2,
        )
    return dict(settings)
