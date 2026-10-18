# Algorithmic Methods of Data Mining — Homework 1

Solutions to Homework 1 (HackerRank Python challenges). Every challenge in the assignment is completed:
**91 challenges in Problem 1** and **6 in Problem 2**.

## Repository content

| Path | What it contains |
|---|---|
| `README.md` | This file: overview and index of every challenge. |
| `scripts.py` | All solutions in one file, grouped by section, one function per challenge. The body of each function is the exact code submitted on HackerRank. |
| `solutions/` | The same solutions as one standalone `.py` file per challenge, ready to run or to paste into HackerRank. |
| `printouts/` | PDF printout of my HackerRank submissions page (`hackerrank_submissions.pdf`) and screenshots of the accepted challenges. |

## Running the code

```bash
python scripts.py list                                   # list all solutions
echo "5" | python scripts.py p1_01_05_python_loops       # run one solution
python solutions/problem1/01_introduction/05_python_loops.py < input.txt
```

Every solution reads from standard input exactly like HackerRank. Templates that write to
`OUTPUT_PATH` print to the terminal when `scripts.py` is used locally.

All solutions were tested locally (Python 3.13.16) on the sample cases from each problem
statement plus extra edge cases, and the algorithms of Problem 2 were also cross-checked against brute-force
implementations on random inputs.

## Problem 1 — Python challenges

| Challenge | File | Function in `scripts.py` |
|---|---|---|
| **Introduction** (7/7, max 75 pts) | | |
| [Say "Hello, World!" With Python](https://www.hackerrank.com/challenges/py-hello-world/problem) | [`01_py_hello_world.py`](solutions/problem1/01_introduction/01_py_hello_world.py) | `p1_01_01_py_hello_world` |
| [Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem) | [`02_py_if_else.py`](solutions/problem1/01_introduction/02_py_if_else.py) | `p1_01_02_py_if_else` |
| [Arithmetic Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem) | [`03_python_arithmetic_operators.py`](solutions/problem1/01_introduction/03_python_arithmetic_operators.py) | `p1_01_03_python_arithmetic_operators` |
| [Python: Division](https://www.hackerrank.com/challenges/python-division/problem) | [`04_python_division.py`](solutions/problem1/01_introduction/04_python_division.py) | `p1_01_04_python_division` |
| [Loops](https://www.hackerrank.com/challenges/python-loops/problem) | [`05_python_loops.py`](solutions/problem1/01_introduction/05_python_loops.py) | `p1_01_05_python_loops` |
| [Write a function](https://www.hackerrank.com/challenges/write-a-function/problem) | [`06_write_a_function.py`](solutions/problem1/01_introduction/06_write_a_function.py) | `p1_01_06_write_a_function` |
| [Print Function](https://www.hackerrank.com/challenges/python-print/problem) | [`07_python_print.py`](solutions/problem1/01_introduction/07_python_print.py) | `p1_01_07_python_print` |
| **Basic Data Types** (6/6, max 60 pts) | | |
| [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem) | [`01_list_comprehensions.py`](solutions/problem1/02_basic_data_types/01_list_comprehensions.py) | `p1_02_01_list_comprehensions` |
| [Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem) | [`02_find_second_maximum_number_in_a_list.py`](solutions/problem1/02_basic_data_types/02_find_second_maximum_number_in_a_list.py) | `p1_02_02_find_second_maximum_number_in_a_list` |
| [Nested Lists](https://www.hackerrank.com/challenges/nested-list/problem) | [`03_nested_list.py`](solutions/problem1/02_basic_data_types/03_nested_list.py) | `p1_02_03_nested_list` |
| [Finding the percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem) | [`04_finding_the_percentage.py`](solutions/problem1/02_basic_data_types/04_finding_the_percentage.py) | `p1_02_04_finding_the_percentage` |
| [Lists](https://www.hackerrank.com/challenges/python-lists/problem) | [`05_python_lists.py`](solutions/problem1/02_basic_data_types/05_python_lists.py) | `p1_02_05_python_lists` |
| [Tuples](https://www.hackerrank.com/challenges/python-tuples/problem) | [`06_python_tuples.py`](solutions/problem1/02_basic_data_types/06_python_tuples.py) | `p1_02_06_python_tuples` |
| **Strings** (14/14, max 220 pts) | | |
| [sWAP cASE](https://www.hackerrank.com/challenges/swap-case/problem) | [`01_swap_case.py`](solutions/problem1/03_strings/01_swap_case.py) | `p1_03_01_swap_case` |
| [String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem) | [`02_python_string_split_and_join.py`](solutions/problem1/03_strings/02_python_string_split_and_join.py) | `p1_03_02_python_string_split_and_join` |
| [What's Your Name?](https://www.hackerrank.com/challenges/whats-your-name/problem) | [`03_whats_your_name.py`](solutions/problem1/03_strings/03_whats_your_name.py) | `p1_03_03_whats_your_name` |
| [Mutations](https://www.hackerrank.com/challenges/python-mutations/problem) | [`04_python_mutations.py`](solutions/problem1/03_strings/04_python_mutations.py) | `p1_03_04_python_mutations` |
| [Find a string](https://www.hackerrank.com/challenges/find-a-string/problem) | [`05_find_a_string.py`](solutions/problem1/03_strings/05_find_a_string.py) | `p1_03_05_find_a_string` |
| [String Validators](https://www.hackerrank.com/challenges/string-validators/problem) | [`06_string_validators.py`](solutions/problem1/03_strings/06_string_validators.py) | `p1_03_06_string_validators` |
| [Text Alignment](https://www.hackerrank.com/challenges/text-alignment/problem) | [`07_text_alignment.py`](solutions/problem1/03_strings/07_text_alignment.py) | `p1_03_07_text_alignment` |
| [Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem) | [`08_text_wrap.py`](solutions/problem1/03_strings/08_text_wrap.py) | `p1_03_08_text_wrap` |
| [Designer Door Mat](https://www.hackerrank.com/challenges/designer-door-mat/problem) | [`09_designer_door_mat.py`](solutions/problem1/03_strings/09_designer_door_mat.py) | `p1_03_09_designer_door_mat` |
| [String Formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem) | [`10_python_string_formatting.py`](solutions/problem1/03_strings/10_python_string_formatting.py) | `p1_03_10_python_string_formatting` |
| [Alphabet Rangoli](https://www.hackerrank.com/challenges/alphabet-rangoli/problem) | [`11_alphabet_rangoli.py`](solutions/problem1/03_strings/11_alphabet_rangoli.py) | `p1_03_11_alphabet_rangoli` |
| [Capitalize!](https://www.hackerrank.com/challenges/capitalize/problem) | [`12_capitalize.py`](solutions/problem1/03_strings/12_capitalize.py) | `p1_03_12_capitalize` |
| [The Minion Game](https://www.hackerrank.com/challenges/the-minion-game/problem) | [`13_the_minion_game.py`](solutions/problem1/03_strings/13_the_minion_game.py) | `p1_03_13_the_minion_game` |
| [Merge the Tools!](https://www.hackerrank.com/challenges/merge-the-tools/problem) | [`14_merge_the_tools.py`](solutions/problem1/03_strings/14_merge_the_tools.py) | `p1_03_14_merge_the_tools` |
| **Sets** (13/13, max 170 pts) | | |
| [Introduction to Sets](https://www.hackerrank.com/challenges/py-introduction-to-sets/problem) | [`01_py_introduction_to_sets.py`](solutions/problem1/04_sets/01_py_introduction_to_sets.py) | `p1_04_01_py_introduction_to_sets` |
| [No Idea!](https://www.hackerrank.com/challenges/no-idea/problem) | [`02_no_idea.py`](solutions/problem1/04_sets/02_no_idea.py) | `p1_04_02_no_idea` |
| [Symmetric Difference](https://www.hackerrank.com/challenges/symmetric-difference/problem) | [`03_symmetric_difference.py`](solutions/problem1/04_sets/03_symmetric_difference.py) | `p1_04_03_symmetric_difference` |
| [Set .add()](https://www.hackerrank.com/challenges/py-set-add/problem) | [`04_py_set_add.py`](solutions/problem1/04_sets/04_py_set_add.py) | `p1_04_04_py_set_add` |
| [Set .discard(), .remove() & .pop()](https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem) | [`05_py_set_discard_remove_pop.py`](solutions/problem1/04_sets/05_py_set_discard_remove_pop.py) | `p1_04_05_py_set_discard_remove_pop` |
| [Set .union() Operation](https://www.hackerrank.com/challenges/py-set-union/problem) | [`06_py_set_union.py`](solutions/problem1/04_sets/06_py_set_union.py) | `p1_04_06_py_set_union` |
| [Set .intersection() Operation](https://www.hackerrank.com/challenges/py-set-intersection-operation/problem) | [`07_py_set_intersection_operation.py`](solutions/problem1/04_sets/07_py_set_intersection_operation.py) | `p1_04_07_py_set_intersection_operation` |
| [Set .difference() Operation](https://www.hackerrank.com/challenges/py-set-difference-operation/problem) | [`08_py_set_difference_operation.py`](solutions/problem1/04_sets/08_py_set_difference_operation.py) | `p1_04_08_py_set_difference_operation` |
| [Set .symmetric_difference() Operation](https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem) | [`09_py_set_symmetric_difference_operation.py`](solutions/problem1/04_sets/09_py_set_symmetric_difference_operation.py) | `p1_04_09_py_set_symmetric_difference_operation` |
| [Set Mutations](https://www.hackerrank.com/challenges/py-set-mutations/problem) | [`10_py_set_mutations.py`](solutions/problem1/04_sets/10_py_set_mutations.py) | `p1_04_10_py_set_mutations` |
| [The Captain's Room](https://www.hackerrank.com/challenges/py-the-captains-room/problem) | [`11_py_the_captains_room.py`](solutions/problem1/04_sets/11_py_the_captains_room.py) | `p1_04_11_py_the_captains_room` |
| [Check Subset](https://www.hackerrank.com/challenges/py-check-subset/problem) | [`12_py_check_subset.py`](solutions/problem1/04_sets/12_py_check_subset.py) | `p1_04_12_py_check_subset` |
| [Check Strict Superset](https://www.hackerrank.com/challenges/py-check-strict-superset/problem) | [`13_py_check_strict_superset.py`](solutions/problem1/04_sets/13_py_check_strict_superset.py) | `p1_04_13_py_check_strict_superset` |
| **Collections** (8/8, max 220 pts) | | |
| [collections.Counter()](https://www.hackerrank.com/challenges/collections-counter/problem) | [`01_collections_counter.py`](solutions/problem1/05_collections/01_collections_counter.py) | `p1_05_01_collections_counter` |
| [DefaultDict Tutorial](https://www.hackerrank.com/challenges/defaultdict-tutorial/problem) | [`02_defaultdict_tutorial.py`](solutions/problem1/05_collections/02_defaultdict_tutorial.py) | `p1_05_02_defaultdict_tutorial` |
| [Collections.namedtuple()](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem) | [`03_py_collections_namedtuple.py`](solutions/problem1/05_collections/03_py_collections_namedtuple.py) | `p1_05_03_py_collections_namedtuple` |
| [Collections.OrderedDict()](https://www.hackerrank.com/challenges/py-collections-ordereddict/problem) | [`04_py_collections_ordereddict.py`](solutions/problem1/05_collections/04_py_collections_ordereddict.py) | `p1_05_04_py_collections_ordereddict` |
| [Word Order](https://www.hackerrank.com/challenges/word-order/problem) | [`05_word_order.py`](solutions/problem1/05_collections/05_word_order.py) | `p1_05_05_word_order` |
| [Collections.deque()](https://www.hackerrank.com/challenges/py-collections-deque/problem) | [`06_py_collections_deque.py`](solutions/problem1/05_collections/06_py_collections_deque.py) | `p1_05_06_py_collections_deque` |
| [Company Logo](https://www.hackerrank.com/challenges/most-commons/problem) | [`07_most_commons.py`](solutions/problem1/05_collections/07_most_commons.py) | `p1_05_07_most_commons` |
| [Piling Up!](https://www.hackerrank.com/challenges/piling-up/problem) | [`08_piling_up.py`](solutions/problem1/05_collections/08_piling_up.py) | `p1_05_08_piling_up` |
| **Date and Time** (2/2, max 40 pts) | | |
| [Calendar Module](https://www.hackerrank.com/challenges/calendar-module/problem) | [`01_calendar_module.py`](solutions/problem1/06_date_and_time/01_calendar_module.py) | `p1_06_01_calendar_module` |
| [Time Delta](https://www.hackerrank.com/challenges/python-time-delta/problem) | [`02_python_time_delta.py`](solutions/problem1/06_date_and_time/02_python_time_delta.py) | `p1_06_02_python_time_delta` |
| **Errors and Exceptions** (1/1, max 10 pts) | | |
| [Exceptions](https://www.hackerrank.com/challenges/exceptions/problem) | [`01_exceptions.py`](solutions/problem1/07_exceptions/01_exceptions.py) | `p1_07_01_exceptions` |
| **Built-Ins** (3/3, max 80 pts) | | |
| [Zipped!](https://www.hackerrank.com/challenges/zipped/problem) | [`01_zipped.py`](solutions/problem1/08_built_ins/01_zipped.py) | `p1_08_01_zipped` |
| [Athlete Sort](https://www.hackerrank.com/challenges/python-sort-sort/problem) | [`02_python_sort_sort.py`](solutions/problem1/08_built_ins/02_python_sort_sort.py) | `p1_08_02_python_sort_sort` |
| [ginortS](https://www.hackerrank.com/challenges/ginorts/problem) | [`03_ginorts.py`](solutions/problem1/08_built_ins/03_ginorts.py) | `p1_08_03_ginorts` |
| **Python Functionals** (1/1, max 20 pts) | | |
| [Map and Lambda Function](https://www.hackerrank.com/challenges/map-and-lambda-expression/problem) | [`01_map_and_lambda_expression.py`](solutions/problem1/09_python_functionals/01_map_and_lambda_expression.py) | `p1_09_01_map_and_lambda_expression` |
| **Regex and Parsing** (17/17, max 560 pts) | | |
| [Detect Floating Point Number](https://www.hackerrank.com/challenges/introduction-to-regex/problem) | [`01_introduction_to_regex.py`](solutions/problem1/10_regex_and_parsing/01_introduction_to_regex.py) | `p1_10_01_introduction_to_regex` |
| [Re.split()](https://www.hackerrank.com/challenges/re-split/problem) | [`02_re_split.py`](solutions/problem1/10_regex_and_parsing/02_re_split.py) | `p1_10_02_re_split` |
| [Group(), Groups() & Groupdict()](https://www.hackerrank.com/challenges/re-group-groups/problem) | [`03_re_group_groups.py`](solutions/problem1/10_regex_and_parsing/03_re_group_groups.py) | `p1_10_03_re_group_groups` |
| [Re.findall() & Re.finditer()](https://www.hackerrank.com/challenges/re-findall-re-finditer/problem) | [`04_re_findall_re_finditer.py`](solutions/problem1/10_regex_and_parsing/04_re_findall_re_finditer.py) | `p1_10_04_re_findall_re_finditer` |
| [Re.start() & Re.end()](https://www.hackerrank.com/challenges/re-start-re-end/problem) | [`05_re_start_re_end.py`](solutions/problem1/10_regex_and_parsing/05_re_start_re_end.py) | `p1_10_05_re_start_re_end` |
| [Regex Substitution](https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem) | [`06_re_sub_regex_substitution.py`](solutions/problem1/10_regex_and_parsing/06_re_sub_regex_substitution.py) | `p1_10_06_re_sub_regex_substitution` |
| [Validating Roman Numerals](https://www.hackerrank.com/challenges/validate-a-roman-number/problem) | [`07_validate_a_roman_number.py`](solutions/problem1/10_regex_and_parsing/07_validate_a_roman_number.py) | `p1_10_07_validate_a_roman_number` |
| [Validating phone numbers](https://www.hackerrank.com/challenges/validating-the-phone-number/problem) | [`08_validating_the_phone_number.py`](solutions/problem1/10_regex_and_parsing/08_validating_the_phone_number.py) | `p1_10_08_validating_the_phone_number` |
| [Validating and Parsing Email Addresses](https://www.hackerrank.com/challenges/validating-named-email-addresses/problem) | [`09_validating_named_email_addresses.py`](solutions/problem1/10_regex_and_parsing/09_validating_named_email_addresses.py) | `p1_10_09_validating_named_email_addresses` |
| [Hex Color Code](https://www.hackerrank.com/challenges/hex-color-code/problem) | [`10_hex_color_code.py`](solutions/problem1/10_regex_and_parsing/10_hex_color_code.py) | `p1_10_10_hex_color_code` |
| [HTML Parser - Part 1](https://www.hackerrank.com/challenges/html-parser-part-1/problem) | [`11_html_parser_part_1.py`](solutions/problem1/10_regex_and_parsing/11_html_parser_part_1.py) | `p1_10_11_html_parser_part_1` |
| [HTML Parser - Part 2](https://www.hackerrank.com/challenges/html-parser-part-2/problem) | [`12_html_parser_part_2.py`](solutions/problem1/10_regex_and_parsing/12_html_parser_part_2.py) | `p1_10_12_html_parser_part_2` |
| [Detect HTML Tags, Attributes and Attribute Values](https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem) | [`13_detect_html_tags_attributes_and_attribute_values.py`](solutions/problem1/10_regex_and_parsing/13_detect_html_tags_attributes_and_attribute_values.py) | `p1_10_13_detect_html_tags_attributes_and_attribute_values` |
| [Validating UID](https://www.hackerrank.com/challenges/validating-uid/problem) | [`14_validating_uid.py`](solutions/problem1/10_regex_and_parsing/14_validating_uid.py) | `p1_10_14_validating_uid` |
| [Validating Credit Card Numbers](https://www.hackerrank.com/challenges/validating-credit-card-number/problem) | [`15_validating_credit_card_number.py`](solutions/problem1/10_regex_and_parsing/15_validating_credit_card_number.py) | `p1_10_15_validating_credit_card_number` |
| [Validating Postal Codes](https://www.hackerrank.com/challenges/validating-postalcode/problem) | [`16_validating_postalcode.py`](solutions/problem1/10_regex_and_parsing/16_validating_postalcode.py) | `p1_10_16_validating_postalcode` |
| [Matrix Script](https://www.hackerrank.com/challenges/matrix-script/problem) | [`17_matrix_script.py`](solutions/problem1/10_regex_and_parsing/17_matrix_script.py) | `p1_10_17_matrix_script` |
| **XML** (2/2, max 40 pts) | | |
| [XML 1 - Find the Score](https://www.hackerrank.com/challenges/xml-1-find-the-score/problem) | [`01_xml_1_find_the_score.py`](solutions/problem1/11_xml/01_xml_1_find_the_score.py) | `p1_11_01_xml_1_find_the_score` |
| [XML2 - Find the Maximum Depth](https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem) | [`02_xml2_find_the_maximum_depth.py`](solutions/problem1/11_xml/02_xml2_find_the_maximum_depth.py) | `p1_11_02_xml2_find_the_maximum_depth` |
| **Closures and Decorators** (2/2, max 60 pts) | | |
| [Standardize Mobile Number Using Decorators](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem) | [`01_standardize_mobile_number_using_decorators.py`](solutions/problem1/12_closures_and_decorators/01_standardize_mobile_number_using_decorators.py) | `p1_12_01_standardize_mobile_number_using_decorators` |
| [Decorators 2 - Name Directory](https://www.hackerrank.com/challenges/decorators-2-name-directory/problem) | [`02_decorators_2_name_directory.py`](solutions/problem1/12_closures_and_decorators/02_decorators_2_name_directory.py) | `p1_12_02_decorators_2_name_directory` |
| **Numpy** (15/15, max 300 pts) | | |
| [Arrays](https://www.hackerrank.com/challenges/np-arrays/problem) | [`01_np_arrays.py`](solutions/problem1/13_numpy/01_np_arrays.py) | `p1_13_01_np_arrays` |
| [Shape and Reshape](https://www.hackerrank.com/challenges/np-shape-reshape/problem) | [`02_np_shape_reshape.py`](solutions/problem1/13_numpy/02_np_shape_reshape.py) | `p1_13_02_np_shape_reshape` |
| [Transpose and Flatten](https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem) | [`03_np_transpose_and_flatten.py`](solutions/problem1/13_numpy/03_np_transpose_and_flatten.py) | `p1_13_03_np_transpose_and_flatten` |
| [Concatenate](https://www.hackerrank.com/challenges/np-concatenate/problem) | [`04_np_concatenate.py`](solutions/problem1/13_numpy/04_np_concatenate.py) | `p1_13_04_np_concatenate` |
| [Zeros and Ones](https://www.hackerrank.com/challenges/np-zeros-and-ones/problem) | [`05_np_zeros_and_ones.py`](solutions/problem1/13_numpy/05_np_zeros_and_ones.py) | `p1_13_05_np_zeros_and_ones` |
| [Eye and Identity](https://www.hackerrank.com/challenges/np-eye-and-identity/problem) | [`06_np_eye_and_identity.py`](solutions/problem1/13_numpy/06_np_eye_and_identity.py) | `p1_13_06_np_eye_and_identity` |
| [Array Mathematics](https://www.hackerrank.com/challenges/np-array-mathematics/problem) | [`07_np_array_mathematics.py`](solutions/problem1/13_numpy/07_np_array_mathematics.py) | `p1_13_07_np_array_mathematics` |
| [Floor, Ceil and Rint](https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem) | [`08_floor_ceil_and_rint.py`](solutions/problem1/13_numpy/08_floor_ceil_and_rint.py) | `p1_13_08_floor_ceil_and_rint` |
| [Sum and Prod](https://www.hackerrank.com/challenges/np-sum-and-prod/problem) | [`09_np_sum_and_prod.py`](solutions/problem1/13_numpy/09_np_sum_and_prod.py) | `p1_13_09_np_sum_and_prod` |
| [Min and Max](https://www.hackerrank.com/challenges/np-min-and-max/problem) | [`10_np_min_and_max.py`](solutions/problem1/13_numpy/10_np_min_and_max.py) | `p1_13_10_np_min_and_max` |
| [Mean, Var, and Std](https://www.hackerrank.com/challenges/np-mean-var-and-std/problem) | [`11_np_mean_var_and_std.py`](solutions/problem1/13_numpy/11_np_mean_var_and_std.py) | `p1_13_11_np_mean_var_and_std` |
| [Dot and Cross](https://www.hackerrank.com/challenges/np-dot-and-cross/problem) | [`12_np_dot_and_cross.py`](solutions/problem1/13_numpy/12_np_dot_and_cross.py) | `p1_13_12_np_dot_and_cross` |
| [Inner and Outer](https://www.hackerrank.com/challenges/np-inner-and-outer/problem) | [`13_np_inner_and_outer.py`](solutions/problem1/13_numpy/13_np_inner_and_outer.py) | `p1_13_13_np_inner_and_outer` |
| [Polynomials](https://www.hackerrank.com/challenges/np-polynomials/problem) | [`14_np_polynomials.py`](solutions/problem1/13_numpy/14_np_polynomials.py) | `p1_13_14_np_polynomials` |
| [Linear Algebra](https://www.hackerrank.com/challenges/np-linear-algebra/problem) | [`15_np_linear_algebra.py`](solutions/problem1/13_numpy/15_np_linear_algebra.py) | `p1_13_15_np_linear_algebra` |

## Problem 2 — Algorithms

| Challenge | File | Function in `scripts.py` |
|---|---|---|
| [Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles/problem) | [`01_birthday_cake_candles.py`](solutions/problem2_algorithms/01_birthday_cake_candles.py) | `p2_01_birthday_cake_candles` |
| [Number Line Jumps (Kangaroo)](https://www.hackerrank.com/challenges/kangaroo/problem) | [`02_kangaroo.py`](solutions/problem2_algorithms/02_kangaroo.py) | `p2_02_kangaroo` |
| [Viral Advertising](https://www.hackerrank.com/challenges/strange-advertising/problem) | [`03_strange_advertising.py`](solutions/problem2_algorithms/03_strange_advertising.py) | `p2_03_strange_advertising` |
| [Recursive Digit Sum](https://www.hackerrank.com/challenges/recursive-digit-sum/problem) | [`04_recursive_digit_sum.py`](solutions/problem2_algorithms/04_recursive_digit_sum.py) | `p2_04_recursive_digit_sum` |
| [Insertion Sort - Part 1](https://www.hackerrank.com/challenges/insertionsort1/problem) | [`05_insertionsort1.py`](solutions/problem2_algorithms/05_insertionsort1.py) | `p2_05_insertionsort1` |
| [Insertion Sort - Part 2](https://www.hackerrank.com/challenges/insertionsort2/problem) | [`06_insertionsort2.py`](solutions/problem2_algorithms/06_insertionsort2.py) | `p2_06_insertionsort2` |

## Notes

- **Tuples** — Prints the hash HackerRank expects (3713081631934410656 for the sample) in both Python 3 and PyPy 3.
- **Numpy** (Arrays, Eye and Identity, Floor, Ceil and Rint) — `numpy.set_printoptions(legacy='1.13')` makes float arrays print in the old
  format (`[ 1.  0.]`) that HackerRank's expected output uses.

## Academic honesty

I did not look at the solutions/editorials provided by HackerRank.
The solutions were written with the help of an AI assistant (Claude).
