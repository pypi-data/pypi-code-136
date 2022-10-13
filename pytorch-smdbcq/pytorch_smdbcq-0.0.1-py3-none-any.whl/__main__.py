from . import SMDBCQ

if __name__ == "__main__":
    import argparse

    def demo():
        try:
            from d3rlpy.datasets import get_cartpole
        except:
            print("Demo requires the package `d3rlpy`. Please install with: `python3 -m pip install d3rlpy`.")
            exit()
        import numpy as np

        import torch
        from torch.utils.data import TensorDataset, DataLoader

        data = get_cartpole()[0]
        k = torch.from_numpy(np.ones(data.rewards.shape))[:-1]
        state = torch.from_numpy(data.observations)[:-1]
        action = torch.from_numpy(data.actions).long()[:-1].unsqueeze(-1)
        next_state = torch.from_numpy(data.observations)[1:]
        reward = torch.from_numpy(data.rewards)[:-1]
        not_done = torch.from_numpy(~data.terminals.astype(bool))[:-1]
        dataset = TensorDataset(k, state, action, next_state, reward, not_done)
        dl = DataLoader(dataset, batch_size=args.batch_size)
        model = SMDBCQ(num_actions=2,
                       state_dim=state.shape[-1],
                       device=args.device)
        for epoch in range(args.num_epochs):
            print(f"Beginning epoch {epoch}...")
            for batch in dl:
                loss = model.train(batch)
        print("Saving model weights...")
        model.save(args.output_filename)

    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", default=False, required=False, action="store_true")
    parser.add_argument("--num_epochs", default=1, type=int, help="Number of training epochs")
    parser.add_argument("--batch_size", default=32, type=int, help="Size of training batches")
    parser.add_argument("--output_filename", default="cartpole.pt", help="Model weights output filename")
    parser.add_argument("--device", type=str, default="cpu", help="`cpu` (default) or `cuda` (for GPU use)")
    args = parser.parse_args()

    if args.demo:
        demo()
