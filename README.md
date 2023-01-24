# Schedule Notifier

Schedule Notifier is a simple tool to create cron job in a [telegram bot](https://t.me/cron_telebot). It is written in Python and uses the telegram bot to send notifications.

----

## Installaion
### Installing Dependencies
### Method 1 : Automated Script
```bash
curl -s https://raw.githubusercontent.com/git-clone-abhinav/ScheduleNotifier/master/install.sh | bash
```

### Method 2 : Download and use virtual environment
```bash
$ git clone https://github.com/git-clone-abhinav/ScheduleNotifier.git
$ cd ScheduleNotifier
$ source venv/bin/activate
```

### Method 3 : Download and install the requirements manually.
```bash
$ git clone https://github.com/git-clone-abhinav/ScheduleNotifier.git
$ cd ScheduleNotifier
$ pip3 install -r requirements.txt
```

### Create a `schedule.csv` according to the format given below. You can use [this](https://crontab.guru/) tool for generating cron notation.
```csv
TaskName, TaskMessage, CronJobNotation
PhysicsTest, Revise for the test daily, 0 16 * * *
JoggingTime, Jogging for 30 minutes, 0 7 * * *
MedicalCheckup, Checkup for the month, 0 15 1 */6 *
```
here, `TaskName` is the name of the task, `TaskMessage` is the definition of the task and `CronJobNotation` is the cron notation for the task. Place `\n` for new line in the `TaskMessage` for a new line in the message.

`0 15 1 */6 *` means every 6 months on the 1st day of the month at 15:00. For more details follow the below conventions or the [man page](https://crontab.guru/crontab.5.html)

#### Cron Notations
| Field name | Mandatory? | Allowed values | Allowed special characters |
| ---------- | ---------- | -------------- | -------------------------- |
| Minutes | Yes | 0-59 | * / , - |
| Hours | Yes | 0-23 | * / , - |
| Day of month | Yes | 1-31 | * / , - ? |
| Month | Yes | 1-12 or JAN-DEC | * / , - |
| Day of week | Yes | 0-6 or SUN-SAT | * / , - ? |
| Year | No | 1970–2099 | * / , - |

`*` means any value

`/` means every n values

`,` means specific values

`-` means a range of values

`?` means no specific value


#### Examples
| Expression | Equivalent To |
| ---------- | ------------- |
| 5 0 * * * | run five minutes after midnight, every day |
| 15 14 1 * * | run at 2:15pm on the first of every month |
| 0 22 * * 1-5 | run at 10 pm on weekdays |
| 23 0-23/2 * * * | run 23 minutes after midn, 2am, 4am ..., everyday |
| 5 4 * * sun |     run at 5 after 4 every sunday |

[More Cron Notation Examples](https://crontab.guru/examples.html)


You can also use the `schedule.csv.exmaple` provided in the repository and rename it to `schedule.csv`

----

## Usage

```bash
$ python3 main.py
```

----

### Requirements
- `Python 3.6` or above
- `pyautogui`

----

## Credits
 All credits to [Chua Hui Shun](https://github.com/huishun98) for her [telegram bot](https://t.me/cron_telebot). I'd really appreciate if you guys give her a follow her on [medium](https://huishun.medium.com/). Check out her code [here](https://github.com/hsdevelops/rm-bot.git)
 
 <img src="https://avatars.githubusercontent.com/u/25633486?v=4" alt="Chua Hui Shun" style="height: 75px; width: 75px ;border-radius: 50% ;margin: 10px ;"/>