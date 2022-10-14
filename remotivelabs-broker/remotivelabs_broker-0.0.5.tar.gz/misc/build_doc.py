import pdoc
import remotivelabs.broker as br
from argparse import ArgumentParser

if __name__ == '__main__':

    # Arguments
    ap = ArgumentParser(description='PDoc generator')
    ap.add_argument('--out',
                    required=True,
                    nargs=1)
    args = ap.parse_args()
    print('Building documentation to {}...'.format(args.out))

    # Parse
    doc = pdoc.doc.Module(br)
    pdoc.render.configure(
            favicon='https://releases.remotivelabs.com/favicon.ico',
            logo='https://releases.remotivelabs.com/remotive-labs-logo-neg.png',
            template_directory='doc/theme')
    html = pdoc.render.html_module(module=doc, all_modules={"remotivelabs.broker": doc})

    print('Stamping with version {}.'.format(br.version))

