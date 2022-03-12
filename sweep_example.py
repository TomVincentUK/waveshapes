"""
=============
Sweep example
=============

A script that uses `waveshapes`  to play a sweep between two frequencies,
specified by `freq_sweep_endpoints`, which lasts `duration` seconds and fades
both in and out.

I wrote this script before I wrote the module, to function as a template for
how a `waveshapes` script should be called.

Once this script behaves as expected it can be safely deleted, or repurposed as
an example script for documentation.
"""
import numpy as np
import waveshapes as ws

# Input parameters for frequency sweep
chunk_size = 64  # samples
sample_rate = 44100  # Hz
duration = 5  # s
max_volume = 0.5  # fraction of maximum output amplitude
freq_sweep_endpoints = 880, 440  # Hz

# Generate frequencies and amplitude envelope for every sample
freq = np.geomspace(*freq_sweep_endpoints, duration * sample_rate)
t = np.linspace(0, duration, duration * sample_rate, endpoint=False)
amp = max_volume * np.sin(np.pi * t / duration) ** 2

# Create audio scene
scene = ws.Scene(chunk_size=chunk_size, sample_rate=sample_rate)

# Add a stereo output with an amp node connected to both inputs
output = ws.outputs.DACStereo(scene=scene)
amp = ws.basic.Product(scene=scene, outlets=[output.inlets["R"], output.inlets["L"]])

# Create the oscillator to play the sweep
osc = ws.oscillators.Sine(scene=scene, outlets=[amp.inlets.new()])

# Create readers to pass data from arrays to the oscillator and amp node
osc_freq = ws.inputs.ArrayReader(scene=scene, array=freq, outlets=[osc.inlets["freq"]])
osc_amp = ws.inputs.ArrayReader(scene=scene, array=amp, outlets=[amp.inlets.new()])

# Run the scene and stop after `duration` seconds
scene.run(duration=duration)
