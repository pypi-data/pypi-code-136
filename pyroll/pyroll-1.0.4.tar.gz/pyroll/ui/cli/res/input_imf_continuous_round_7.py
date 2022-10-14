from pyroll.core import CircularOvalGroove, RoundGroove, Roll, Profile, RollPass, Transport, SwedishOvalGroove

# initial profile
in_profile = Profile.round(
    radius=24e-3,
    temperature=1200 + 273.15,
    strain=0,
    material="C45",
    flow_stress=100e6
)



# pass sequence
sequence = [
    RollPass(
        label="K 02/001 - 1",
        roll=Roll(
            groove=SwedishOvalGroove(
                r1=6e-3,
                r2=26e-3,
                ground_width=38e-3,
                usable_width=60e-3,
                depth=7.25e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9
        ),
        velocity=1,
        gap=13.5e-3,
    ),
    Transport(
        duration=6.4
    ),
    RollPass(
        label="K 05/001 - 2",
        roll=Roll(
            groove=RoundGroove(
                r1=4e-3,
                r2=18e-3,
                depth=17.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9
        ),
        velocity=1,
        gap=1.5e-3,
    ),
    Transport(
        duration=3.6
    ),
    RollPass(
        label="K 02/001 - 3",
        roll=Roll(
            groove=SwedishOvalGroove(
                r1=6e-3,
                r2=26e-3,
                ground_width=38e-3,
                usable_width=60e-3,
                depth=7.25e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9
        ),
        velocity=2,
        gap=1.5e-3,
    ),
    Transport(
        duration=3.4
    ),
    RollPass(
        label="K 05/002 - 4",
        roll=Roll(
            groove=RoundGroove(
                r1=4e-3,
                r2=13.5e-3,
                depth=12.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9
        ),
        velocity=2,
        gap=1e-3,
    ),
    Transport(
        duration=5.2
    ),
    RollPass(
        label="K 03/001 - 5",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=6e-3,
                r2=38e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9
        ),
        velocity=2,
        gap=5.4e-3,
    ),
    Transport(
        duration=4.4
    ),
    RollPass(
        label="K 05/003 - 6",
        roll=Roll(
            groove=RoundGroove(
                r1=3e-3,
                r2=10e-3,
                depth=9e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9
        ),
        velocity=2,
        gap=1.8e-3,
    ),
    Transport(
        duration=3.8
    ),
    RollPass(
        label="K 03/001 - 7",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=6e-3,
                r2=38e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
        ),
        velocity=2,
        gap=0.8e-3,
    ),
    Transport(
        duration=7.2
    ),
    RollPass(
        label="K 05/004 - 8",
        roll=Roll(
            groove=RoundGroove(
                r1=2e-3,
                r2=7.5e-3,
                depth=5.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
        ),
        velocity=2,
        gap=3.8e-3,
    ),
    Transport(
        duration=6.2
    ),
    RollPass(
        label="K 03/002 - 9",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=6e-3,
                r2=21.2e-3,
                depth=2.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
        ),
        velocity=2,
        gap=3.5e-3,
    ),
    Transport(
        duration=4.5
    ), RollPass(
        label="K 05/005 - 10",
        roll=Roll(
            groove=RoundGroove(
                r1=0.5e-3,
                r2=6e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
        ),
        velocity=2,
        gap=4e-3,
    ),
    Transport(
        duration=9
    ),
    RollPass(
        label="F1 - K 3/50",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=2.5e-3,
                r2=12.5e-3,
                depth=2.9e-3
            ),
            nominal_radius=107.5e-3,
            youngs_modulus=210e9
        ),
        velocity=4.89,
        gap=1.2e-3,
    ),
    Transport(
        duration=1.5 / 4.89
    ),
    RollPass(
        label="F2 - K 9/28",
        roll=Roll(
            groove=RoundGroove(
                r1=0.5e-3,
                r2=4e-3,
                depth=4e-3
            ),
            nominal_radius=107.5e-3,
            youngs_modulus=210e9
        ),
        velocity=6.1,
        gap=2.1e-3,
    ),
    Transport(
        duration=1.5 / 6.1
    ),
    RollPass(
        label="F3 - K3/51",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=2.5e-3,
                r2=11e-3,
                depth=2.12e-3
            ),
            nominal_radius=107.5e-3,
            youngs_modulus=210e9
        ),
        velocity=7.91,
        gap=1.3e-3,
    ),
    Transport(
        duration=1.5 / 7.91
    ),
    RollPass(
        label="F4 - K9/29",
        roll=Roll(
            groove=RoundGroove(
                r1=0.5e-3,
                r2=3.57e-3,
                depth=2.75e-3
            ),
            nominal_radius=85e-3,
            youngs_modulus=210e9
        ),
        velocity=10,
        gap=1.5e-3,
    ),
]
