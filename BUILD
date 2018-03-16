py_binary(
    name = "ft_vgg",
    srcs = ["ft_vgg.py"],
    data = [
        "train.txt",
    ],
    imports = [
        "external/models/research/slim",
    ],
    deps = [
        "@models//research/slim:nets",
        "@models//research/slim:preprocessing_factory",
    ],
)

py_binary(
    name = "gen_train_val",
    srcs = ["gen_train_val.py"],
)
