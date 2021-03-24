from behave import when
import subprocess
import constants


@when("I run {command} with flags {flags}")
def step_impl(context, command, flags):
    f = flags.split(" ")
    run_command(context, command, f)


@when("I run {command}")
def step_impl(context, command):
    run_command(context, command)


def run_command(context, command, flags=None):
    if command not in constants.WHITELIST:
        raise Exception(f"ERROR: Command '{command}' not in whitelist.")
    args = [command]
    if flags is not None:
        [args.append(f) for f in flags]
    p = subprocess.Popen(command)
    stdout, stderr = p.communicate()
    context.data["last_run_args"] = args
    context.data["last_run_stdout"] = stdout
    context.data["last_run_stderr"] = stderr

