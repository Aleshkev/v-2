import logging
import pathlib
import subprocess
import sys

logger = logging.getLogger(__name__)


def render(content: pathlib.Path, root_url: str, output: pathlib.Path):
    for adoc_file in content.glob('*.adoc'):
        logger.info(f"Rendering {adoc_file}")

        out = output / (adoc_file.stem + '.html')

        subprocess.run([
            'asciidoctor',
            '--destination-dir', str(output),
            '-a', 'linkcss',
            '-a', 'docinfo=shared',
            str(adoc_file)
        ], shell=True, stdout=sys.stdout)
