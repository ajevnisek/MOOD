def get_single_line_tinyImagenet(id_dataset='cifar10',
                                 network_name='MadrysResnet',
                                 training_type='Classical-Training'):
    model_path_prefix = 'ID-CIFAR-10' if id_dataset == 'cifar10' else 'ID-CIFAR-100'
    return f"python main.py --id {id_dataset} --od T -ms odin -mc jpg --arch " \
           f"{network_name} " \
           f"--file final_models/{model_path_prefix}-{network_name}-" \
           f"{training_type}.pth > " \
           f"Tiny_logs/{model_path_prefix}-{network_name}" \
           f"-{training_type}-Tiny.log"
def get_single_line_cifar10_as_ood(id_dataset='cifar100',
                                 network_name='MadrysResnet',
                                 training_type='Classical-Training'):
    model_path_prefix = 'ID-CIFAR-10' if id_dataset == 'cifar10' else 'ID-CIFAR-100'
    return f"python main.py --id {id_dataset} --od 10 -ms odin -mc jpg --arch " \
           f"{network_name} " \
           f"--file final_models/{model_path_prefix}-{network_name}-" \
           f"{training_type}.pth > " \
           f"cifar10_as_ood_logs/{model_path_prefix}-{network_name}" \
           f"-{training_type}-cifar10-as-ood.log"

def get_single_line_cifar100_as_ood(id_dataset='cifar10',
                                 network_name='MadrysResnet',
                                 training_type='Classical-Training'):
    model_path_prefix = 'ID-CIFAR-10' if id_dataset == 'cifar10' else 'ID-CIFAR-100'
    return f"python main.py --id {id_dataset} --od 100 -ms odin -mc jpg " \
           f"--arch " \
           f"{network_name} " \
           f"--file final_models/{model_path_prefix}-{network_name}-" \
           f"{training_type}.pth > " \
           f"cifar100_as_ood_logs/{model_path_prefix}-{network_name}" \
           f"-{training_type}-cifar100-as-ood.log"

final_line_to_run = ""
for id in [
    # 'cifar10',
    'cifar100']:
    for nn_name in ['MadrysResnet', 'ResNet18', 'ResNet34']:
        for training_type in ['Classical-Training', 'GQ']:
            # print(get_single_line_tinyImagenet(id, nn_name, training_type))
            final_line_to_run += get_single_line_tinyImagenet(id, nn_name, training_type)
            final_line_to_run += ' ; '
print("=" * 30)
print(final_line_to_run)

final_line_to_run = ""
for id in [
    # 'cifar10',
    'cifar100']:
    for nn_name in ['MadrysResnet', 'ResNet18', 'ResNet34']:
        for training_type in ['Classical-Training', 'GQ']:
            # print(get_single_line_tinyImagenet(id, nn_name, training_type))
            final_line_to_run += get_single_line_cifar10_as_ood(id, nn_name, training_type)
            final_line_to_run += ' ; '
print("=" * 30)
print(final_line_to_run)

final_line_to_run = ""
for id in [
    'cifar10',
    # 'cifar100'
]:
    for nn_name in ['MadrysResnet', 'ResNet18', 'ResNet34']:
        for training_type in ['Classical-Training', 'GQ']:
            # print(get_single_line_tinyImagenet(id, nn_name, training_type))
            final_line_to_run += get_single_line_cifar100_as_ood(id, nn_name,
                                                                 training_type)
            final_line_to_run += ' ; '
print("=" * 30)
print(final_line_to_run)