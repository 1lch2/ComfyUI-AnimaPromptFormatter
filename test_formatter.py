"""
AnimaPromptFormatter - Test Script

Validates the formatting function correctness.
"""

from utils import format_prompt


def test_format_prompt():
    """Test various formatting scenarios"""
    
    print("=" * 60)
    print("AnimaPromptFormatter Test")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        # (input, expected, description)
        ("", "", "Empty string"),
        ("tag1", "tag1", "Single tag"),
        ("tag1,tag2", "tag1, tag2", "Two tags no space"),
        ("tag1, tag2", "tag1, tag2", "Two tags with correct space"),
        ("tag1 , tag2", "tag1, tag2", "Space before comma"),
        ("tag1,  tag2", "tag1, tag2", "Multiple spaces after comma"),
        ("tag1,,tag2", "tag1, tag2", "Consecutive commas"),
        ("tag1,,,tag2", "tag1, tag2", "Multiple consecutive commas"),
        ("tag1\ntag2", "tag1 tag2", "Newline character"),
        ("tag1\r\ntag2", "tag1 tag2", "Windows newline"),
        ("tag1,tag2\ntag3,tag4", "tag1, tag2 tag3, tag4", "Multi-line mixed"),
        ("  tag1  ,  tag2  ", "tag1, tag2", "Leading/trailing spaces"),
        (",tag1,tag2,", "tag1, tag2", "Leading/trailing commas"),
        ("   ", "", "Only spaces"),
        (",,,", "", "Only commas"),
        ("a beautiful landscape, sunset, mountains, peaceful", 
         "a beautiful landscape, sunset, mountains, peaceful", 
         "Natural language mixed"),
    ]
    
    passed = 0
    failed = 0
    
    for i, (input_text, expected, description) in enumerate(test_cases, 1):
        result = format_prompt(input_text)
        status = "[PASS]" if result == expected else "[FAIL]"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\nTest {i}: {description}")
        print(f"  Input:   {repr(input_text)}")
        print(f"  Expected: {repr(expected)}")
        print(f"  Result:   {repr(result)}")
        print(f"  Status:   {status}")
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = test_format_prompt()
    exit(0 if success else 1)
