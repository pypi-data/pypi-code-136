#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-tts-plugin-pico = ovos_tts_plugin_pico:PicoTTS'
SAMPLE_CONFIGS = 'ovos-tts-plugin-pico.config = ovos_tts_plugin_pico:PicoTTSPluginConfig'

setup(
    name='ovos-tts-plugin-pico',
    version='0.0.4a2',
    description='pico tts plugin for mycroft',
    url='https://github.com/OpenVoiceOS/ovos-tts-plugin-pico',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_tts_plugin_pico'],
    install_requires=['ovos-plugin-manager>=0.0.1a12'],
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft OpenVoiceOS OVOS chatterbox plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT,
                  'mycroft.plugin.tts.config': SAMPLE_CONFIGS}
)
