genrule(
    name = "package",
    srcs = ["//src:main"],
    outs = ["package.tar.gz"],
    cmd = "$(location //tools:pack) --bin $(location //src:main) --output $(OUTS)",
    tools = ["//tools:pack"],
)
