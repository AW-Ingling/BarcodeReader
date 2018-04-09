// Win32Project2.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"


using namespace Platform;
using namespace Windows::Devices::Input;
using namespace Windows::Foundation;
using namespace Windows::Foundation::Collections;


extern "C" {

	__declspec(dllexport) double TimesTwo(double x, double y)
	{
		double z = x * y;

		return z;
	}




}



