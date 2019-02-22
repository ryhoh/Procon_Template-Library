project(testLibrary)

add_executable(testLibrary testLibrary.cc)

target_link_libraries(testLibrary
        gtest
        gtest_main
        pthread)