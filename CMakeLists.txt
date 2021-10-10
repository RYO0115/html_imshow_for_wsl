
# Cmake version
cmake_minimum_required(VERSION 3.0)

# Project Name and Language
project(html_imshow VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_FLAGS "-O2 -Wall -pthread")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)

# Add Subdirectory
#add_subdirectory(src)

# Add Include dir
#target_include_directories(
#	new_object_detection
#	${PROJECT_SOURCE_DIR}/include
#)

include_directories(
	${PROJECT_SOURCE_DIR}/include
    ${OpenCV_INCLUDE_DIRS}
)

link_directories(
	${PROJECT_SOURCE_DIR}
)

add_library(html_imshow STATIC src/html_imshow.cpp)

install(TARGETS html_imshow
    EXPORT html_imshow-config
    DESTINATION lib/cmake/html_imshow

    # 静的ライブラリのインストール先
    ARCHIVE DESTINATION lib
    # 共有ライブラリのインストール先
    LIBRARY DESTINATION lib
)

install(FILES 
    include/html_imshow.hpp
    DESTINATION include/html_imshow
)

include(CMakePackageConfigHelpers)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/html_imshow-config-version.cmake
    COMPATIBILITY SameMajorVersion
)

install(FILES 
    ${CMAKE_CURRENT_BINARY_DIR}/html_imshow-config-version.cmake
    DESTINATION lib/cmake/html_imshow
)

install(EXPORT html_imshow-config
    DESTINATION lib/cmake/html_imshow
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
    DESTINATION include
)


add_executable(
    html_test
    test/test.cpp
)
target_link_libraries(
    html_test    
    html_imshow
)


## Test code
#add_executable(opencv_tester
#    src/opencv_tester.cpp
#)

#target_link_libraries(
#    opencv_tester
#    ${OpenCV_LIBRARIES}
#)
