from d2l import torch as d2l
import torch

class LinearRegressionScratch(d2l.Module):
    """The linear regression model implemented from scratch."""
    def __init__(self, num_inputs, lr, sigma=0.01):
        super().__init__()
        self.save_hyperparameters()
        self.w = torch.normal(0, sigma, (num_inputs, 1), requires_grad=True)
        self.b = torch.zeros(1, requires_grad=True)

    def forward(self, X):
        """here, torch.matmul() is performing a matrix-vector multiplication rather than a dot product"""
        return torch.matmul(X, self.w) + self.b
    
    def loss(self, y_hat, y):
        l = (y_hat - y) ** 2 / 2
        return l.mean()
    
    def configure_optimizers(self):
        return SGD([self.w, self.b], self.lr)
    
class SGD(d2l.HyperParameters):
    """Minibatch stochastic gradient descent."""
    def __init__(self, params, lr):
        self.save_hyperparameters()
    
    def step(self):
        """Update the parameters"""
        for param in self.params:
            params -= self.lr * param.grad
    
    def zero_grad(self):
        """Sets all gradients to 0, which must be run before a backpropagation step"""
        for param in self.params:
            if param.grad is not None:
                param.grad.zero_()