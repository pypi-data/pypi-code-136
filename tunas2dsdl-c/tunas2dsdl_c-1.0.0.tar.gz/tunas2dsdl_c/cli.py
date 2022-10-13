import os
import click
from tunas2dsdl_c.dsdl_yaml_script import ConvertV3toDsdlYaml


@click.command()
@click.option("-s", "--src_dir", "src_dir", type=str, required=True,
              help="source file path: eg./Users/jiangyiying/sherry/tunas_data_demo/CIFAR10-tunas")
@click.option("-o", "--out_dir", "out_dir", type=str, default=None,
              help="out file path: eg./Users/jiangyiying/sherry/tunas_data_demo/CIFAR10-dsdl")
@click.option("-c", "--unique_cate", "unique_cate", type=str, default="category_name",
              help="use which field as unique category name, default is 'category_name', "
                   "if 'category_name' has duplicated value, you need to change it. Else leave it alone.")
@click.option("-l", "--local", "local", is_flag=True,
              help="bool type: use where to put samples, default is sample.json, "
                    "if you use `-l` will put samples in the same file of definition file")
def convert(src_dir, out_dir, unique_cate, local):
    assert os.path.isdir(src_dir), f"The source dir '{src_dir}' is not a directory."
    print(f"your input source dictionary: {src_dir}")
    print(f"your input destination dictionary: {out_dir}")
    v3toyaml = ConvertV3toDsdlYaml(src_dir, out_dir, unique_cate, local)
    v3toyaml.convert_pipeline()


@click.group()
def cli():
    pass


cli.add_command(convert)

if __name__ == '__main__':
    cli()
