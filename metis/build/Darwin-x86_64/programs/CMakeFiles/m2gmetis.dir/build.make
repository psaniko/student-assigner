# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Produce verbose output by default.
VERBOSE = 1

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.17.0_1/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.17.0_1/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kim/Desktop/stu/metis-5.1.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64

# Include any dependencies generated for this target.
include programs/CMakeFiles/m2gmetis.dir/depend.make

# Include the progress variables for this target.
include programs/CMakeFiles/m2gmetis.dir/progress.make

# Include the compile flags for this target's objects.
include programs/CMakeFiles/m2gmetis.dir/flags.make

programs/CMakeFiles/m2gmetis.dir/m2gmetis.c.o: programs/CMakeFiles/m2gmetis.dir/flags.make
programs/CMakeFiles/m2gmetis.dir/m2gmetis.c.o: ../../programs/m2gmetis.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object programs/CMakeFiles/m2gmetis.dir/m2gmetis.c.o"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/m2gmetis.dir/m2gmetis.c.o   -c /Users/kim/Desktop/stu/metis-5.1.0/programs/m2gmetis.c

programs/CMakeFiles/m2gmetis.dir/m2gmetis.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/m2gmetis.dir/m2gmetis.c.i"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kim/Desktop/stu/metis-5.1.0/programs/m2gmetis.c > CMakeFiles/m2gmetis.dir/m2gmetis.c.i

programs/CMakeFiles/m2gmetis.dir/m2gmetis.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/m2gmetis.dir/m2gmetis.c.s"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kim/Desktop/stu/metis-5.1.0/programs/m2gmetis.c -o CMakeFiles/m2gmetis.dir/m2gmetis.c.s

programs/CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.o: programs/CMakeFiles/m2gmetis.dir/flags.make
programs/CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.o: ../../programs/cmdline_m2gmetis.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object programs/CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.o"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.o   -c /Users/kim/Desktop/stu/metis-5.1.0/programs/cmdline_m2gmetis.c

programs/CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.i"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kim/Desktop/stu/metis-5.1.0/programs/cmdline_m2gmetis.c > CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.i

programs/CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.s"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kim/Desktop/stu/metis-5.1.0/programs/cmdline_m2gmetis.c -o CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.s

programs/CMakeFiles/m2gmetis.dir/io.c.o: programs/CMakeFiles/m2gmetis.dir/flags.make
programs/CMakeFiles/m2gmetis.dir/io.c.o: ../../programs/io.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object programs/CMakeFiles/m2gmetis.dir/io.c.o"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/m2gmetis.dir/io.c.o   -c /Users/kim/Desktop/stu/metis-5.1.0/programs/io.c

programs/CMakeFiles/m2gmetis.dir/io.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/m2gmetis.dir/io.c.i"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/kim/Desktop/stu/metis-5.1.0/programs/io.c > CMakeFiles/m2gmetis.dir/io.c.i

programs/CMakeFiles/m2gmetis.dir/io.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/m2gmetis.dir/io.c.s"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/kim/Desktop/stu/metis-5.1.0/programs/io.c -o CMakeFiles/m2gmetis.dir/io.c.s

# Object files for target m2gmetis
m2gmetis_OBJECTS = \
"CMakeFiles/m2gmetis.dir/m2gmetis.c.o" \
"CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.o" \
"CMakeFiles/m2gmetis.dir/io.c.o"

# External object files for target m2gmetis
m2gmetis_EXTERNAL_OBJECTS =

programs/m2gmetis: programs/CMakeFiles/m2gmetis.dir/m2gmetis.c.o
programs/m2gmetis: programs/CMakeFiles/m2gmetis.dir/cmdline_m2gmetis.c.o
programs/m2gmetis: programs/CMakeFiles/m2gmetis.dir/io.c.o
programs/m2gmetis: programs/CMakeFiles/m2gmetis.dir/build.make
programs/m2gmetis: libmetis/libmetis.dylib
programs/m2gmetis: programs/CMakeFiles/m2gmetis.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking C executable m2gmetis"
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/m2gmetis.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
programs/CMakeFiles/m2gmetis.dir/build: programs/m2gmetis

.PHONY : programs/CMakeFiles/m2gmetis.dir/build

programs/CMakeFiles/m2gmetis.dir/clean:
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs && $(CMAKE_COMMAND) -P CMakeFiles/m2gmetis.dir/cmake_clean.cmake
.PHONY : programs/CMakeFiles/m2gmetis.dir/clean

programs/CMakeFiles/m2gmetis.dir/depend:
	cd /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kim/Desktop/stu/metis-5.1.0 /Users/kim/Desktop/stu/metis-5.1.0/programs /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64 /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs /Users/kim/Desktop/stu/metis-5.1.0/build/Darwin-x86_64/programs/CMakeFiles/m2gmetis.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : programs/CMakeFiles/m2gmetis.dir/depend

