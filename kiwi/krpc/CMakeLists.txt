cmake_minimum_required(VERSION 3.17)
project(krpc)

add_executable(krpc main.cc ${SOURCES_AND_HEADERS})
target_include_directories(
    ${PROJECT_NAME}
    PUBLIC ${PROJECT_SOURCE_DIR}/kiwi/include
)

include(FetchContent)

FetchContent_Declare(
    json
    GIT_REPOSITORY https://github.com/nlohmann/json.git
    GIT_TAG v3.11.2
)

FetchContent_MakeAvailable(json)

target_link_libraries(krpc PRIVATE nlohmann_json::nlohmann_json)