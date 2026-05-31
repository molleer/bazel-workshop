load("@rules_cc//cc:cc_test.bzl", "cc_test")

cc_test(
    name = "main_test",
    size = "small",
    srcs = ["main_test.cc"],
    deps = [
        "//src:main",
        "@googletest//:gtest",
        "@googletest//:gtest_main",
    ],
)
