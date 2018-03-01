# TIMEC Sentinel

An all-powerful toolset for TIMEC.

Sentinel is an autonomous agent for persisting, processing and automating TIME 1.0.0.0 governance objects and
tasks

Sentinel is implemented as a Python application that binds to a local version 1.0.0.0 timed instance on each TIMEC v1.0.0.0 Masternode.

This guide covers installing Sentinel onto an existing 1.0.0.0 Masternode in Ubuntu 14.04 / 16.04.

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install virtualenv

Make sure the local TIME daemon running is at least version 1.0.0 (100000)

    $ time-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/loony383/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with timed and the installation is complete
Run the sentinel once. It may pause for up to 30 seconds before returning. There should be no output in a normal return

    $ ./venv/bin/python bin/sentinel.py

Adjust access rights to the sentinel database

    $ chmod -R 755 database

### 4. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >> sentinel.log 2>&1

## Configuration

An alternative (non-default) path to the `time.conf` file can be specified in `sentinel.conf`:

    time_conf=/path/to/time.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

### License

Released under the MIT license, under the same terms as TIMECore itself. See [LICENSE](LICENSE) for more info.
