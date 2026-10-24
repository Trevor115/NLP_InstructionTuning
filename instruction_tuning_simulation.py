"""
From Prompting to Instruction Tuning - Student Template

Name: Trevor Tourdot
Date: 10/24/2026

"""

from dataclasses import dataclass
from typing import List


@dataclass
class ExperimentResult:
    task_name: str
    prompt_type: str
    prompt_text: str
    model_output: str
    followed_instructions: bool
    notes: str


# -----------------------------
# PRINTING FUNCTIONS
# -----------------------------
def print_result(result: ExperimentResult) -> None:
    print("=" * 70)
    print(f"Task: {result.task_name}")
    print(f"Prompt Type: {result.prompt_type}")

    print("\nPrompt:")
    print(result.prompt_text)

    print("\nModel Output:")
    print(result.model_output)

    print(f"\nFollowed Instructions: {result.followed_instructions}")
    print(f"Notes: {result.notes}")
    print("=" * 70)
    print()


def compare_results(prompt_only: ExperimentResult,
                    instruction_tuned: ExperimentResult) -> None:

    print("#" * 70)
    print(f"COMPARISON FOR TASK: {prompt_only.task_name}")
    print("#" * 70)

    print("\nPrompt Only Output:")
    print(prompt_only.model_output)

    print("\nInstruction Tuned Output:")
    print(instruction_tuned.model_output)

    print("\nAnalysis:")

    if prompt_only.task_name == "Translation":
        print(
            "The model successfully translated the phrase in both versions. "
            "However, the instruction tuned version followed the expected "
            "format more precisely because the examples established a clear "
            "pattern for the response."
        )

        print(
            "\nPerformance improved slightly because the output was more "
            "consistent and aligned with the requested format. The examples "
            "helped guide the model toward producing only the translation."
        )

    elif prompt_only.task_name == "Summarization":
        print(
            "Both outputs correctly summarized the paragraph, but the "
            "instruction tuned version produced a shorter and more focused "
            "summary. The examples demonstrated the desired level of brevity."
        )

        print(
            "\nPerformance improved because the model followed the specific "
            "one sentence format. The provided examples showed exactly how "
            "the summary should be structured."
        )

    elif prompt_only.task_name == "Explanation":
        print(
            "The prompt only output explained gravity correctly, but the "
            "instruction tuned version used language that was easier for a "
            "young child to understand. It better matched the intended audience."
        )

        print(
            "\nThis task showed the greatest improvement because the examples "
            "demonstrated how to simplify difficult concepts. The model was "
            "better able to adjust its tone and vocabulary for a child."
        )

    print()


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main() -> None:
    results: List[ExperimentResult] = []

    # ===================================================
    # TASK 1 (REQUIRED)
    # ===================================================

    # Prompts
    prompt_only_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Prompt Only",
        prompt_text="Translate to Spanish: Good morning",
        model_output="Buenos días.",
        followed_instructions=True,
        notes="Correct translation was provided."
    )

    instruction_1 = ExperimentResult(
        task_name="Translation",
        prompt_type="Instruction Tuned",
        prompt_text=(
            "Instruction: Translate to Spanish\n"
            "Input: Hello\n"
            "Output: Hola\n\n"
            "Instruction: Translate to Spanish\n"
            "Input: Thank you\n"
            "Output: Gracias\n\n"
            "Instruction: Translate to Spanish\n"
            "Input: Good morning\n"
            "Output:"
        ),
        model_output="Buenos días",
        followed_instructions=True,
        notes="Correct translation provided in the exact format requested."
    )

    results.append(prompt_only_1)
    results.append(instruction_1)

    # ===================================================
    # TASK 2 (REQUIRED)
    # ===================================================

    prompt_only_2 = ExperimentResult(
        task_name="Summarization",
        prompt_type="Prompt Only",
        prompt_text=(
            "Summarize the following paragraph: "
            "Artificial intelligence is changing many industries by automating "
            "repetitive tasks and improving decision making."
        ),
        model_output=(
            "Artificial intelligence is helping industries become more efficient "
            "through automation and better decision making."
        ),
        followed_instructions=True,
        notes="Produced an accurate summary."
    )

    instruction_2 = ExperimentResult(
        task_name="Summarization",
        prompt_type="Instruction Tuned",
        prompt_text=(
            "Instruction: Summarize the text in one sentence.\n"
            "Input: Online learning lets students learn from anywhere.\n"
            "Output: Online learning enables remote education.\n\n"
            "Instruction: Summarize the text in one sentence.\n"
            "Input: Artificial intelligence is changing many industries by automating repetitive tasks and improving decision making.\n"
            "Output:"
        ),
        model_output=(
            "Artificial intelligence improves industries through automation "
            "and enhanced decision making."
        ),
        followed_instructions=True,
        notes="Generated a concise one sentence summary as instructed."
    )

    results.append(prompt_only_2)
    results.append(instruction_2)

    # ===================================================
    # TASK 3 (REQUIRED)
    # ===================================================

    prompt_only_3 = ExperimentResult(
        task_name="Explanation",
        prompt_type="Prompt Only",
        prompt_text="Explain gravity to a 6 year old.",
        model_output=(
            "Gravity is a force that pulls objects toward the Earth. "
            "It keeps us from floating away."
        ),
        followed_instructions=True,
        notes="Correct explanation but uses somewhat advanced language."
    )

    instruction_3 = ExperimentResult(
        task_name="Explanation",
        prompt_type="Instruction Tuned",
        prompt_text=(
            "Instruction: Explain a concept to a young child.\n"
            "Input: What is rain?\n"
            "Output: Rain is water that falls from clouds in the sky.\n\n"
            "Instruction: Explain a concept to a young child.\n"
            "Input: What is gravity?\n"
            "Output:"
        ),
        model_output=(
            "Gravity is like an invisible helper that keeps your feet on the "
            "ground and makes things fall instead of floating away."
        ),
        followed_instructions=True,
        notes="More child friendly explanation that closely follows the examples."
    )

    results.append(prompt_only_3)
    results.append(instruction_3)

    # ===================================================
    # REQUIRED FAILURE CASE
    # ===================================================

    failure_case = ExperimentResult(
        task_name="Failure Case",
        prompt_type="Instruction Tuned",
        prompt_text=(
            "Instruction: Count the number of r's in a word.\n"
            "Input: carrot\n"
            "Output: 2\n\n"
            "Instruction: Count the number of r's in a word.\n"
            "Input: strawberry\n"
            "Output:"
        ),
        model_output="2",
        followed_instructions=False,
        notes=(
            "The correct answer is 3.\n"
            "- The model incorrectly counted the letters.\n"
            "- It misunderstood the character level task.\n"
            "- The output is incorrect even though the format is correct.\n"
            "- Instruction tuning helps with following patterns and formatting, "
            "but it does not guarantee accurate reasoning."
        )
    )

    results.append(failure_case)

    # ===================================================
    # PRINT RESULTS
    # ===================================================
    print("\nALL RESULTS\n")

    for result in results:
        print_result(result)

    # ===================================================
    # COMPARISONS
    # ===================================================
    compare_results(prompt_only_1, instruction_1)
    compare_results(prompt_only_2, instruction_2)
    compare_results(prompt_only_3, instruction_3)


if __name__ == "__main__":
    main()