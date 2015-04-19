// addon.cc
#include <node.h>
#include "size.h"

using namespace v8;

void Init(Handle<Object> exports) {
  NODE_SET_METHOD(exports,"terminalSize",terminalSize);
}

NODE_MODULE(terminal_size, Init)
