#include <SPIRV/SpvBuilder.h>

int main()
{
    spv::SpvBuildLogger logger;
    spv::Builder builder(1, 1, &logger);

    builder.setSourceFile("source.spv");

    return 0;
}
