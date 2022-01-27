#include <iostream>
#include <pybind11/pybind11.h>

namespace py = pybind11;

void receive_data() {
	std::cout << "Data received!" << std::endl;
}

PYBIND11_MODULE(bindings, m) {
	m.def("receive_data", &receive_data, "Hello");
}
