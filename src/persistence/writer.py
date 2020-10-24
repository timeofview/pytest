SERVICES_FILE = 'services.csv'

output_data = None


def write_configs(configs_file, configs):
    file = open(configs_file, "w")
    for config in configs:
        file.write(config.to_string() + '\n')
    file.close()


def write_services(services_file, services):
    file = open(services_file, "a")
    for service in services:
        file.write(service.to_string() + '\n')
    file.close()


def write_service(services_file, service):
    services_file.write(service.to_string() + '\n')


def get_service_file(services_file=SERVICES_FILE):
    return open(services_file, "a")


def write_groups(groups_file, groups):
    file = open(groups_file, "w")
    for group in groups:
        file.write(group.to_string() + '\n')
    file.close()
