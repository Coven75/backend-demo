import logging

import coloredlogs


def load_logger():
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])

    level_styles = {
        'debug': {'color': 'blue'},
        'info': {'color': 'green'},
        'warning': {'color': 'yellow'},
        'error': {'color': 'red'},
        'critical': {'color': 'red', 'bold': True},
    }

    # Define custom colors for log fields
    field_styles = {
        'asctime': {'color': 'cyan'},
        'levelname': {'color': 'green', 'bold': True}
    }

    coloredlogs.install(level='INFO', fmt=log_format, level_styles=level_styles, field_styles=field_styles)
    logger = logging.getLogger(__name__)
