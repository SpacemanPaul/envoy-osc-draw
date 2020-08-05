import math
import random

from utils import animate_keyvals, animator_keyvals

random.seed()

background = {"background": [0, 0, 0, 128]}
grids = {
    "lines": [
                 {
                     "colour": [16, 36, 84, 150],
                     "points": [[x, 0], [x, 1]],
                     "width": "2px",
                     "curve": False,
                     "close": False
                 }
                 for x in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)
             ] + [
                 {
                     "colour": [16, 36, 84, 150],
                     "points": [[0, x], [1, x]],
                     "width": "2px",
                     "curve": False,
                     "close": False
                 }
                 for x in [0.5, 0.67777, 0.32222, 0.8555, 0.1444]
             ]
}

grid2 = {
    "lines": [
        {
            "colour": "red",
            "points": [[0, 0], ["100px", "50%"]],
            "width": "1.5px"
        },
        {
            "colour": "red",
            "points": [[1, 0], [0.2, 0.4]],
            "width": "3px"
        }
    ],
}


def sine_callback(x, resolution, state, phase, period, amplitude):
    # period of 1.0 = 1 screen width
    period *= resolution[0]
    phase *= period
    # Amplitude of 1.0 = full screen height
    amplitude *= resolution[1]
    return math.sin(2 * math.pi * (x + phase) / period) * amplitude


sinewaves_new = {
    "functions": [
        {
            # "origin": [0, 0.5],
            "function": sine_callback,
            "parameters": {
                "period": 1,
                "phase": lambda state: state["frame_p"],
                "amplitude": 0.25,
            },
            "colour": [66, 255, 112],
            "width": "4px",
            "glow": True,
            "glow_scale": 9,
            "glow_color": [66, 219, 112]
        }
    ]
}


def multiband_callback(x, resolution, state, bands):
    y = 0.0
    for band in bands:
        period, amplitude, phase = band
        if amplitude < 0.0:
            amplitude *= -1
            phase += 0.5
        y += sine_callback(x, resolution, state, period=period, amplitude=amplitude, phase=phase)
    return y


def singleband_randomiser(frames):
    frame = 0
    out = [
        (0, 0.0),
    ]
    frame += random.randint(5, 12)
    while True:
        sign = random.getrandbits(1)
        amp = random.triangular(0.0, 0.12, 0.06)
        if sign:
            amp *= -1.0
        if frame >= frames:
            out.append((frames, amp))
            return out
        out.append((frame, amp))
        frame += random.randint(2, 12)


band1_vals = singleband_randomiser(1000)
band2_vals = singleband_randomiser(1000)
band3_vals = singleband_randomiser(1000)
band4_vals = singleband_randomiser(1000)
band5_vals = singleband_randomiser(1000)


def multiband_animator(state):
    return [
        (
            1/4, animate_keyvals(band1_vals, state), 0.0
        ),
        (
            1 / 8, animate_keyvals(band2_vals, state), 0.0
        ),
        (
            1 / 12, animate_keyvals(band3_vals, state), 0.0
        ),
        (
            1 / 16, animate_keyvals(band4_vals, state), 0.0
        ),
        (
            1 / 20, animate_keyvals(band5_vals, state), 0.0
        ),
    ]


blipness = [
    True,
    True, False,
    True,
    True, False,
    True, False,
    True,
    True,
    True, False,
    True,
    True, False,
    True,

    True, False,
    True,
    True, False,
    True, False,
    True,
    True,
    True, False,
    True,
    True, False,
    True, False,

    True, False,
    True,
    True, False,
    True,
    True, False,
    True, False,
    True,
    True,
    True, False,
    True,
    True,

    False,
    True, False,
    True, False,
    True,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,

    True, False,
    True,
    True, False,
    True, False,
    True,
    True,
    True, False,
    True,
    True, False,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True, False,
    True,
    True,
    True, False,

]

coefficients = [
    (0.03, -0.02, 0.03, -0.01),
    (-0.02, 0.01, -0.02, 0.03),
    (0.01, -0.02, 0.01, -0.02),
    (-0.04, 0.03, -0.02, 0.02),
    (0.01, -0.02, 0.01, -0.01),
    (-0.03, 0.01, -0.02, 0.03),
]



def multiband_modulator(mb_animator):
    def mb_mod(state):
        frame_mb = mb_animator(state)
        fade_in_factor = animate_keyvals((
            (0, 0.0),
            (150, 0.1),
            (215, 0.3),
            (240, 1.0),
        ), state)
        frame_mb = [ (period, amplitude * fade_in_factor ,phase) for period, amplitude, phase in frame_mb ]
        frame = state["frame"]
        ts = frame / 25
        delay = 9.4
        ts = ts - delay
        if ts < 0.0:
            return frame_mb
        step = int(ts * 8)
        stepness = ts * 8 - step
        coeffs = coefficients[step % 6]
        if blipness[step]:
            if stepness >= 0.2:
                return frame_mb
            else:
                return frame_mb + [
                    (1 / 32, 1.2*coeffs[0], 0),
                    (1 / 64, 1.2*coeffs[1], 0),
                    (1 / 96, 1.2*0.7 * coeffs[2], 0),
                    (1 / 128, 1.2*0.4 * coeffs[3], 0),
                ]
            # return [ (period, 0.0 ,phase) for period, amplitude, phase in frame_mb ]
        return frame_mb

    return mb_mod


multiband_something = {
    "functions": [
        {
            "function": multiband_callback,
            "parameters": {
                "bands": multiband_modulator(multiband_animator),
            },
            "colour": [66, 255, 112],
            "width": "4px",
            "glow": True,
            "glow_scale": 9,
            "glow_color": [66, 219, 112]
        }
    ]
}


def expanding_centre_throb_pts(state):
    delta = animate_keyvals((
        (0, 0.0),
        (1, 0.003),
        (5, 0.01),
        (20, 0.003),
        (40, 0.0)
    ), state)
    return (
        (0.5 - delta, 0.499999),
        (0.5 - delta * 2 / 5, 0.5 - delta * 2 / 5),
        (0.5, 0.5 - delta / 2),
        (0.5 + delta * 2 / 5, 0.5 - delta * 2 / 5),
        (0.5 + delta, 0.5),
        (0.5 + delta * 2 / 5, 0.5 + delta * 2 / 5),
        (0.5, 0.5 + delta / 2),
        (0.5 - delta * 2 / 5, 0.5 + delta * 2 / 5),
        (0.5 - delta, 0.500001),
    )


def expanding_centre_throb_pts_flip(state):
    delta = animate_keyvals((
        (0, 0.0),
        (1, 0.003),
        (5, 0.01),
        (20, 0.003),
        (40, 0.0)
    ), state)
    return (
        (0.5 + delta, 0.499999),
        (0.5 + delta * 2 / 5, 0.5 - delta * 2 / 5),
        (0.5, 0.5 - delta / 2),
        (0.5 - delta * 2 / 5, 0.5 - delta * 2 / 5),
        (0.5 - delta, 0.5),
        (0.5 - delta * 2 / 5, 0.5 + delta * 2 / 5),
        (0.5, 0.5 + delta / 2),
        (0.5 + delta * 2 / 5, 0.5 + delta * 2 / 5),
        (0.5 + delta, 0.500001),
    )


starting_throb = {
    "lines": [
        {
            "colour": [66, 255, 112],
            "width": animator_keyvals((
                (0, 1.0),
                (5, 30.0),
                (20, 1.0),
                (40, 1.0)
            )),
            "glow": True,
            "glow_scale": animator_keyvals((
                (0, 0.0),
                (5, 50.0),
                (20, 20.0),
                (40, 8.0)
            )),
            "glow_color": [66, 255, 112],
            "points": expanding_centre_throb_pts,
            "close": False,
        },
        {
            "colour": [66, 255, 112],
            "width": animator_keyvals((
                (0, 1.0),
                (5, 30.0),
                (20, 1.0),
                (40, 1.0)
            )),
            "glow": True,
            "glow_scale": animator_keyvals((
                (0, 0.0),
                (5, 50.0),
                (20, 20.0),
                (40, 8.0)
            )),
            "glow_color": [66, 255, 112],
            "points": expanding_centre_throb_pts_flip,
            "close": False,
        },
    ],
}


def expanding_centre_pts(state):
    delta = animate_keyvals((
        (0, 0.0),
        (5, 0.01),
        (25, 0.5)
    ), state)
    return (
        (0.5 - delta, 0.5),
        (0.5 + delta, 0.5),
    )


expanding_line = {
    "lines": [
        {
            "colour": [66, 255, 112],
            "width": 4.0,
            "glow": True,
            "glow_scale": 10.0,
            "glow_color": [66, 219, 112],
            "points": expanding_centre_pts,
            "close": False
        }
    ]
}

sinewaves = {
    "trigs": [
        {
            "method": "sin",
            "colour": [66, 255, 112],
            "start": [0, 0.5],
            "length": 1,
            "period": 1,
            "amplitude": 0.25,
            "offset": "frame_p * 100%",
            "width": "4px",
            "glow": True,
            "glow_scale": 9,
            "glow_color": [66, 219, 112]
        },
        {
            "method": "sin",
            "colour": [200, 255, 200],
            "start": [0, 0.5],
            "length": 1,
            "period": 1,
            "amplitude": 0.25,
            "offset": "frame_p * 100%",
            "width": "2px",
            "glow": False,
            "glow_scale": 9,
            "glow_color": [66, 219, 112]
        }
    ],
}

sinewaves2 = {
    "trigs": [
        {
            "method": "sin",
            "colour": [66, 219, 112],
            "start": [0, 0.5],
            "length": 1,
            "period": 1,
            "amplitude": 0.25,
            "offset": "frame_p * 100%",
            "width": "2px",
            "glow": True,
            "glow_scale": 9,
            "glow_color": [0, 255, 0]
        },
        {
            "method": "cos",
            "colour": [66, 219, 112],
            "start": [0, 0.5],
            "length": 1,
            "period": 1,
            "amplitude": "35% * math.sin(frame_p * 2 * 2 * math.pi)",
            "offset": "-frame_p * 100%",
            "width": "1.5px",
            "glow": True,
            "glow_scale": 9,
            "glow_color": [0, 255, 0]
        },
        {
            "method": "sin",
            "colour": [66, 219, 112],
            "start": [0, 0.5],
            "length": 1,
            "period": 0.05,
            "amplitude": "45% * math.sin(frame_p * 4 * 2 * math.pi)",
            "offset": "frame_p * 50%",
            "width": "2px",
            "glow": True,
            "glow_scale": 9,
            "glow_color": [0, 255, 0]
        }
    ]
}

multiband = {
    "resolution": [1920, 1080],
    "frames": 900,
    "output": {
        "extname": "png",
        "width": 5,
        "format": "PNG"
    },
    "layers": [
        {
            "type": "still",
            "still": background,
            "mode": "copy"
        },
        {
            "type": "anim",
            "anim": multiband_something,
            "mode": "alpha"
        },
        {
            "disable": True,
            "type": "still",
            "still": grids,
            "mode": "alpha"
        }
    ]
}

start_throb = {
    "resolution": [1920, 1080],
    "frames": 50,
    "output": {
        "basename": "out_",
        "extname": "png",
        "width": 5,
        "format": "PNG"
    },
    "layers": [
        {
            "type": "still",
            "still": background,
            "mode": "copy"
        },
        {
            "type": "anim",
            "anim": starting_throb,
            "mode": "alpha"
        },
        {
            "type": "anim",
            "anim": expanding_line,
            "mode": "alpha"
        }
    ]
}

render = multiband
