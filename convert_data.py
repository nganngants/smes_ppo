import json
import re
from rouge_score import rouge_scorer

def extract_therapist_response(text):
    """Extract only the Therapist's response from the text."""
    match = re.search(r"Therapist's response: (.*?)$", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def calculate_rouge_l(text1, text2):
    """Calculate Rouge-L score between two texts."""
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(text1, text2)
    return scores['rougeL'].fmeasure

def convert_jsonl_to_json(input_file, output_file, threshold=0.7):
    """
    Convert a JSONL file with full content to a JSON file with only Therapist's responses.
    Only include entries where the Rouge-L score between chosen and rejected is below threshold.
    
    Args:
        input_file: Path to the input JSONL file
        output_file: Path to the output JSON file
        threshold: Rouge-L score threshold (lower means more different)
    """
    result = []
    skipped_count = 0
    included_count = 0
    
    # Read JSONL file
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                item = json.loads(line.strip())
                
                # Extract only the Therapist's response
                chosen_response = extract_therapist_response(item.get("chosen", ""))
                rejected_response = extract_therapist_response(item.get("rejected", ""))
                
                # Add to result list only if both responses were found
                if chosen_response and rejected_response:
                    # Calculate Rouge-L score between chosen and rejected
                    rouge_l_score = calculate_rouge_l(chosen_response, rejected_response)
                    
                    # Only include if Rouge-L score is below threshold
                    if rouge_l_score < threshold:
                        result.append({
                            "chosen": chosen_response,
                            "rejected": rejected_response
                        })
                        included_count += 1
                    else:
                        skipped_count += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    
    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"Conversion complete. Processed {included_count + skipped_count} entries.")
    print(f"Included {included_count} entries where Rouge-L score was below {threshold}.")
    print(f"Skipped {skipped_count} entries where Rouge-L score was above or equal to {threshold}.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert JSONL with full content to JSON with only Therapist responses')
    parser.add_argument('--input_file', help='Path to input JSONL file', default="reward_data_train_cut.jsonl", required=False)
    parser.add_argument('--output_file', help='Path to output JSON file', default="reward_data_train_cut.json", required=False)
    parser.add_argument('--threshold', type=float, help='Rouge-L score threshold (lower means more different)', default=0.9)
    
    args = parser.parse_args()
    
    convert_jsonl_to_json(args.input_file, args.output_file, args.threshold)