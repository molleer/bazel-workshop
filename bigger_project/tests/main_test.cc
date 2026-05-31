#include <gtest/gtest.h>
#include "src/main.hh"

TEST(Main, AddTest)
{
    EXPECT_EQ(add(1, 2), 3);
}
