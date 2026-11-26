# === Stage 24: Доля починенного ===
# Project: RepairCafe
from collections import Counter


def repair_success_rate_by_device(applications):
    """Return the fraction of successful repairs grouped by device type.

    Each application is a dict with keys:
        'device'      -> str, e.g. 'phone'
        'master'      -> str
        'date'        -> str
        'success'     -> bool
        'part'        -> str or None

    Returns a dict mapping device name to success rate (0.0..1.0).
    Devices with no applications are omitted.
    """
    device_totals = Counter()
    device_success = Counter()

    for app in applications:
        device = app.get('device')
        if not device:
            continue
        device_totals[device] += 1
        if app.get('success'):
            device_success[device] += 1

    return {
        device: device_success[device] / device_totals[device]
        for device in device_totals
    }


def repair_success_rate_by_device_rounded(applications, precision=2):
    """Return success rates rounded to the given number of decimals."""
    return {
        device: round(rate, precision)
        for device, rate in repair_success_rate_by_device(applications).items()
    }


def main():
    sample = [
        {'device': 'phone', 'master': 'ann', 'date': '2024-01-05', 'success': True,  'part': 'battery'},
        {'device': 'phone', 'master': 'bob', 'date': '2024-01-06', 'success': False, 'part': 'screen'},
        {'device': 'phone', 'master': 'ann', 'date': '2024-01-07', 'success': True,  'part': None},
        {'device': 'laptop', 'master': 'bob', 'date': '2024-01-08', 'success': True,  'part': 'fan'},
        {'device': 'laptop', 'master': 'carol', 'date': '2024-01-09', 'success': False, 'part': None},
        {'device': 'tablet', 'master': 'ann', 'date': '2024-01-10', 'success': True,  'part': 'battery'},
    ]

    print(repair_success_rate_by_device(sample))
    print(repair_success_rate_by_device_rounded(sample))


if __name__ == '__main__':
    main()
