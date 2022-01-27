#pragma once

#include <filesystem>

#include "types.h"

class Binding
{
private:
	path script_path;

public:
	Binding(path script_path_): script_path(script_path_) {}
	void receive_data();
};
