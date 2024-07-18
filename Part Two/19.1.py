import gym
import numpy as np

class PIDController:
    def __init__(self, K_p, K_d, K_i):
        self.K_p = K_p
        self.K_d = K_d
        self.K_i = K_i

    def compute_error(self, track):
        min_distance = float('inf')
        for i in range(len(track)):
            distance = np.linalg.norm(np.array([self.x, self.y])- np.array(track[i]))
            if distance<min_distance:
                min_distance = distance
                error = self.y - track[i][1]  # This error only assumes cte based on y-axis. Further extension is possible

        return error

def main():
    env = gym.make('CartPole-v1')
    pid = PIDController(K_p = 1.0, K_d = 0.0, K_i = 0.1)

    for episode in range(10):
        obs = env.reset()
        reward = 0
        for time in range(1000):
            env.render()
            cart_pos, cart_vel, pole_angle, pole_vel = observation

            control_sig = pid.compute(pole_angle)

            action = 0 if control_sig < 0 else 1

            observation, reward, done, info = env.step(action)
            total_reward += reward

            if done:
                print(f"Episode {episode + 1} finished after {time + 1} timesteps, total reward: {total_reward}")
                break

    env.close()

    

