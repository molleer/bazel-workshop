load("@rules_cc//cc:cc_binary.bzl", "cc_binary")

cc_binary(
    name = "main",
    srcs = [
        "main.cc",
        "main.hh",
    ],
    visibility = ["//src:__pkg__"],
    deps = ["//src/hello"],
)
