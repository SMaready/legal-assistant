cmake_minimum_required(VERSION 3.21)
project(Legal-Assistant LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Automatically run moc, rcc, uic
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

# Tell AUTOUIC where to find .ui files
set(CMAKE_AUTOUIC_SEARCH_PATHS ${CMAKE_SOURCE_DIR}/src/ui)

find_package(Qt6 REQUIRED COMPONENTS
    Core Widgets OpenGL OpenGLWidgets
)

find_package(OpenGL REQUIRED)

# nlohmann/json library to parse JSON
add_subdirectory(third_party/nlohmann_json)

add_subdirectory(src)
