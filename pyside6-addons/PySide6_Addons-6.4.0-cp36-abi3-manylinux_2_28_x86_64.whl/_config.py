built_modules = list(name for name in
    "Core;Gui;Widgets;PrintSupport;Sql;Network;Test;Concurrent;Designer;Xml;Help;Multimedia;MultimediaWidgets;OpenGL;OpenGLWidgets;Pdf;PdfWidgets;Positioning;NetworkAuth;Nfc;Qml;Quick;Quick3D;QuickControls2;QuickWidgets;RemoteObjects;Scxml;Sensors;SerialPort;StateMachine;Charts;SpatialAudio;Svg;SvgWidgets;DataVisualization;Bluetooth;UiTools;WebChannel;WebEngineCore;WebEngineWidgets;WebEngineQuick;WebSockets;HttpServer;DBus;3DCore;3DRender;3DInput;3DLogic;3DAnimation;3DExtras"
    .split(";"))

shiboken_library_soversion = str(6.4)
pyside_library_soversion = str(6.4)

version = "6.4.0"
version_info = (6, 4, 0, "", "")

__build_date__ = '2022-10-11T08:40:54+00:00'




__setup_py_package_version__ = '6.4.0'
