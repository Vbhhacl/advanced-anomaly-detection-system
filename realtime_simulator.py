import time
import random
import requests
import argparse


def run_forever(server_url, interval, seed=None, bounds="-3,3", anomaly_chance=0.05):
    if seed is not None:
        random.seed(seed)

    lo, hi = map(float, bounds.split(","))

    print(f"Starting realtime simulator: {server_url}, interval={interval}s, bounds=[{lo},{hi}], anomaly_chance={anomaly_chance}")
    while True:
        # 95% normal data (from gaussian around 0), 5% outlier samples (anomalies)
        if random.random() < anomaly_chance:
            value = random.choice([random.uniform(hi * 1.5, hi * 2.5), random.uniform(lo * 2.5, lo * 1.5)])
        else:
            value = random.gauss(0, 1)

        payload = {"value": value}
        try:
            r = requests.post(f"{server_url}/predict", json=payload, timeout=2)
            r.raise_for_status()
            out = r.json()
            is_anomaly = out.get("anomaly") == 1
            status = "🚨 ANOMALY" if is_anomaly else "✅ normal"
            print(f"value={value:.4f} -> {status}   (model={out})")

        except requests.RequestException as exc:
            print(f"[ERROR] request failed: {exc}")

        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-time anomaly simulator client")
    parser.add_argument("--url", default="http://127.0.0.1:5000", help="Flask API base URL")
    parser.add_argument("--interval", type=float, default=1.0, help="Seconds between points")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    parser.add_argument("--bounds", default="-3,3", help="Normal value bounds for simulation")
    parser.add_argument("--anomaly-chance", type=float, default=0.05, help="Fraction of outliers to inject")
    args = parser.parse_args()

    run_forever(args.url, args.interval, args.seed, args.bounds, args.anomaly_chance)
