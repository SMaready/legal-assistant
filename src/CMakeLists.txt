set(SOURCES
    main.cpp
    ui/mainwindow.cpp
    bridge/AgentBridge.cpp
    bridge/AgentWorker.cpp
    renderer/GraphWidget.cpp
    renderer/ShaderProgram.cpp
    renderer/GraphLayout.cpp
    renderer/NodeRenderer.cpp
    renderer/EdgeRenderer.cpp
    renderer/Camera2D.cpp
)

set(HEADERS
    ui/mainwindow.h
    bridge/AgentBridge.h
    bridge/AgentWorker.h
    renderer/GraphWidget.h
    renderer/ShaderProgram.h
    renderer/GraphLayout.h
    renderer/NodeRenderer.h
    renderer/EdgeRenderer.h
    renderer/Camera2D.h
)

set(UI_FILES
    ui/mainwindow.ui
)

qt_add_executable(Legal-Assistant
    ${SOURCES} ${HEADERS} ${UI_FILES}
)

target_link_libraries(Legal-Assistant PRIVATE
    Qt6::Core
    Qt6::Widgets
    Qt6::OpenGL
    Qt6::OpenGLWidgets
    OpenGL::GL
    nlohmann_json::nlohmann_json
)

target_compile_definitions(Legal-Assistant PRIVATE
    SHADER_DIR="${CMAKE_SOURCE_DIR}/src/shaders/"
)
