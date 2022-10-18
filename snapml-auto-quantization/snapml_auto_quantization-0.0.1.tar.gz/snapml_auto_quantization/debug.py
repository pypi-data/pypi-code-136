# Our toy network: Mainly two conv layers and three fc layers
import torch.nn as nn
import torch.nn.functional as F
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 8, 5)
        self.bn1 = nn.BatchNorm2d(8)
        self.relu1 = nn.ReLU(inplace=True)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(8, 16, 5)
        self.bn2 = nn.BatchNorm2d(16)
        self.relu2 = nn.ReLU()
        self.fc1 = nn.Linear(16 * 5 * 5, 128)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(128, 64)
        self.relu4 = nn.ReLU()
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = self.pool(self.relu1(self.bn1(self.conv1(x))))
        x = self.pool(self.relu2(self.bn2(self.conv2(x))))
        x = x.view(x.size(0),-1)
        x = self.relu3(self.fc1(x))
        x = self.relu4(self.fc2(x))
        x = self.fc3(x)
        return x

# Dataloaders for train and val 
def get_train_val_dataloaders():
    import torchvision
    import torchvision.transforms as transforms

    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

    valset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
    valloader = torch.utils.data.DataLoader(valset, batch_size=4,
                                         shuffle=False, num_workers=2)

    return trainloader, valloader
    
    
# Training pipeline 
def train_model(model, trainloader, num_epochs, lr=0.003):
    import torch.optim as optim
    import torch.nn as nn
    
    model.train()

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.003, momentum=0.9)
    model.to(device)
    

    for epoch in range(num_epochs):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs
            inputs, labels = data
            if i == 0:
                print(inputs)
                print(labels)
            inputs, labels = inputs.to(device), labels.to(device)

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')

    return model

# Validation pipeline 
def validate_model(model, valloader):
    model.eval()
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)

    correct = 0
    total = 0
    with torch.no_grad():
        for data in valloader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    return 100 * correct / total


# Provide the inference loop function
# Post-training quantization needs to run forward pass on each batch of the training dataset, to compute quantization statistics like the range and zero-point of the layers
def inference_loop_function(model, config):
    dataloader = config["dataloader"]
    model.eval()
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)
    for i, data in enumerate(dataloader, 0):
        # get the inputs
        inputs, labels = data
        inputs, labels = inputs.to(device), labels.to(device)

        outputs = model(inputs)


import torch
import torchvision
import copy

path = "debug.pt"

def run():

    # save the model
    # Network
    net = Net()

    # Dataloaders
    trainloader, valloader = get_train_val_dataloaders()

    # Train the network. 
    # Here for demonstration purpose, we train only 1 epoch. When applying in your own project, you should train your network to convergence.
    net = train_model(net, trainloader, num_epochs=1)


    torch.save({
#            'epoch': EPOCH,
            'model_state_dict': net.state_dict(),
#            'optimizer_state_dict': optimizer.state_dict(),
#            'loss': LOSS,
            }, path)

def load():
    checkpoint = torch.load(path)
    net = Net()
    net.load_state_dict(checkpoint['model_state_dict'])

    trainloader, valloader = get_train_val_dataloaders()

    # Import the QuantizationSimulator from the libary
    from snapml_auto_quantization.quant_simulator import  QuantizationSimulator

    # Initialize the QuantizationSimulator with our trained floating point model
    # We deep copy the model, otherwise it will be overwritten
    quant_sim = QuantizationSimulator(copy.deepcopy(net))

    # Apply post-training quantization with the inference_loop_function defined above as input
    # And it would return the quantized model
    quant_model, quant_sim_model = quant_sim.post_training_quantization(inference_loop_function, 
                                                   config = {"dataloader": trainloader,})

    
    dummy_input = torch.randn(1, 3, 32, 32, dtype=torch.float32)
    input_names = ["data"]
    output_names = ["prob"]

    # Export to onnx format. 
    # You will see warnings like "Warning: Unsupported operator QuantizeSnap. No schema registered for this operator.", which is expected.
    torch.onnx.export(quant_model.to(device='cpu'), dummy_input,
                  'quantized_toy_model.onnx', verbose=False,
                  input_names=input_names, output_names=output_names, 
                  operator_export_type=torch.onnx.OperatorExportTypes.ONNX_ATEN_FALLBACK,
                  enable_onnx_checker=False)

if __name__ == '__main__':
    load()