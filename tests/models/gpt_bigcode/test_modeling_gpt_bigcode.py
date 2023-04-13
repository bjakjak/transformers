# coding=utf-8
<<<<<<< HEAD
# Copyright 2020 The HuggingFace Team. All rights reserved.
=======
# Copyright 2023 The HuggingFace Team. All rights reserved.
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
<<<<<<< HEAD


import datetime
=======
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
import math
import unittest

from parameterized import parameterized
<<<<<<< HEAD
=======

>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
from transformers import GPTBigCodeConfig, is_torch_available
from transformers.testing_utils import require_torch, slow, torch_device

from ...generation.test_utils import GenerationTesterMixin
from ...test_configuration_common import ConfigTester
from ...test_modeling_common import ModelTesterMixin, floats_tensor, ids_tensor, random_attention_mask
<<<<<<< HEAD
=======
from ...test_pipeline_mixin import PipelineTesterMixin
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465


if is_torch_available():
    import torch

    from transformers import (
<<<<<<< HEAD
        GPT_BIGCODE_PRETRAINED_MODEL_ARCHIVE_LIST,
        GPT2Tokenizer,
        GPTBigCodeConfig,
        GPTBigCodeDoubleHeadsModel,
        GPTBigCodeForSequenceClassification,
        GPTBigCodeForTokenClassification,
        GPTBigCodeLMHeadModel,
        GPTBigCodeModel,
    )
    from transformers.models.gpt_bigcode.configuration_gpt_bigcode import AttentionType
=======
        GPT2TokenizerFast,
        GPTBigCodeForCausalLM,
        GPTBigCodeForSequenceClassification,
        GPTBigCodeForTokenClassification,
        GPTBigCodeModel,
    )
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
    from transformers.models.gpt_bigcode.modeling_gpt_bigcode import GPTBigCodeAttention


class GPTBigCodeModelTester:
<<<<<<< HEAD
    # TODO: Update the tests to use valid pretrained models.
=======
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
    def __init__(
        self,
        parent,
        batch_size=14,
        seq_length=7,
        is_training=True,
        use_token_type_ids=True,
        use_input_mask=True,
        use_labels=True,
        use_mc_token_ids=True,
        vocab_size=99,
        hidden_size=32,
        num_hidden_layers=5,
        num_attention_heads=4,
        intermediate_size=37,
<<<<<<< HEAD
        hidden_act="gelu",
=======
        hidden_act="relu",
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=512,
        type_vocab_size=16,
        type_sequence_label_size=2,
        initializer_range=0.02,
        num_labels=3,
        num_choices=4,
<<<<<<< HEAD
=======
        multi_query=True,
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
        scope=None,
    ):
        self.parent = parent
        self.batch_size = batch_size
        self.seq_length = seq_length
        self.is_training = is_training
        self.use_token_type_ids = use_token_type_ids
        self.use_input_mask = use_input_mask
        self.use_labels = use_labels
        self.use_mc_token_ids = use_mc_token_ids
        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.intermediate_size = intermediate_size
        self.hidden_act = hidden_act
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.max_position_embeddings = max_position_embeddings
        self.type_vocab_size = type_vocab_size
        self.type_sequence_label_size = type_sequence_label_size
        self.initializer_range = initializer_range
        self.num_labels = num_labels
        self.num_choices = num_choices
        self.scope = None
        self.bos_token_id = vocab_size - 1
<<<<<<< HEAD
        self.eos_token_id = vocab_size - 1
        self.pad_token_id = vocab_size - 1

    def get_large_model_config(self):
        return GPTBigCodeConfig.from_pretrained("bigcode/santacoder-fast-inference")
=======
        self.eos_token_id = vocab_size - 2
        self.pad_token_id = vocab_size - 3
        self.multi_query = multi_query

    def get_large_model_config(self):
        return GPTBigCodeConfig.from_pretrained("bigcode/gpt_bigcode-santacoder")
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465

    def prepare_config_and_inputs(
        self, gradient_checkpointing=False, scale_attn_by_inverse_layer_idx=False, reorder_and_upcast_attn=False
    ):
        input_ids = ids_tensor([self.batch_size, self.seq_length], self.vocab_size)

        input_mask = None
        if self.use_input_mask:
            input_mask = random_attention_mask([self.batch_size, self.seq_length])

        token_type_ids = None
        if self.use_token_type_ids:
            token_type_ids = ids_tensor([self.batch_size, self.seq_length], self.type_vocab_size)

        mc_token_ids = None
        if self.use_mc_token_ids:
            mc_token_ids = ids_tensor([self.batch_size, self.num_choices], self.seq_length)

        sequence_labels = None
        token_labels = None
        choice_labels = None
        if self.use_labels:
            sequence_labels = ids_tensor([self.batch_size], self.type_sequence_label_size)
            token_labels = ids_tensor([self.batch_size, self.seq_length], self.num_labels)
            choice_labels = ids_tensor([self.batch_size], self.num_choices)

        config = self.get_config(
            gradient_checkpointing=gradient_checkpointing,
            scale_attn_by_inverse_layer_idx=scale_attn_by_inverse_layer_idx,
            reorder_and_upcast_attn=reorder_and_upcast_attn,
        )

        head_mask = ids_tensor([self.num_hidden_layers, self.num_attention_heads], 2)

        return (
            config,
            input_ids,
            input_mask,
            head_mask,
            token_type_ids,
            mc_token_ids,
            sequence_labels,
            token_labels,
            choice_labels,
        )

    def get_config(
        self, gradient_checkpointing=False, scale_attn_by_inverse_layer_idx=False, reorder_and_upcast_attn=False
    ):
        return GPTBigCodeConfig(
            vocab_size=self.vocab_size,
            n_embd=self.hidden_size,
            n_layer=self.num_hidden_layers,
            n_head=self.num_attention_heads,
            n_inner=self.intermediate_size,
            activation_function=self.hidden_act,
            resid_pdrop=self.hidden_dropout_prob,
            attn_pdrop=self.attention_probs_dropout_prob,
            n_positions=self.max_position_embeddings,
            type_vocab_size=self.type_vocab_size,
            initializer_range=self.initializer_range,
            use_cache=True,
            bos_token_id=self.bos_token_id,
            eos_token_id=self.eos_token_id,
            pad_token_id=self.pad_token_id,
            gradient_checkpointing=gradient_checkpointing,
            scale_attn_by_inverse_layer_idx=scale_attn_by_inverse_layer_idx,
            reorder_and_upcast_attn=reorder_and_upcast_attn,
<<<<<<< HEAD
=======
            attention_softmax_in_fp32=False,
            scale_attention_softmax_in_fp32=False,
            multi_query=self.multi_query,
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
        )

    def get_pipeline_config(self):
        config = self.get_config()
        config.vocab_size = 300
        return config

    def prepare_config_and_inputs_for_decoder(self):
        (
            config,
            input_ids,
            input_mask,
            head_mask,
            token_type_ids,
            mc_token_ids,
            sequence_labels,
            token_labels,
            choice_labels,
        ) = self.prepare_config_and_inputs()

        encoder_hidden_states = floats_tensor([self.batch_size, self.seq_length, self.hidden_size])
        encoder_attention_mask = ids_tensor([self.batch_size, self.seq_length], vocab_size=2)

        return (
            config,
            input_ids,
            input_mask,
            head_mask,
            token_type_ids,
            sequence_labels,
            token_labels,
            choice_labels,
            encoder_hidden_states,
            encoder_attention_mask,
        )

    def create_and_check_gpt_bigcode_model(self, config, input_ids, input_mask, head_mask, token_type_ids, *args):
        model = GPTBigCodeModel(config=config)
        model.to(torch_device)
        model.eval()

        result = model(input_ids, token_type_ids=token_type_ids, head_mask=head_mask)
        result = model(input_ids, token_type_ids=token_type_ids)
        result = model(input_ids)

        self.parent.assertEqual(result.last_hidden_state.shape, (self.batch_size, self.seq_length, self.hidden_size))
        self.parent.assertEqual(len(result.past_key_values), config.n_layer)

    def create_and_check_gpt_bigcode_model_past(self, config, input_ids, input_mask, head_mask, token_type_ids, *args):
        model = GPTBigCodeModel(config=config)
        model.to(torch_device)
        model.eval()

        # first forward pass
        outputs = model(input_ids, token_type_ids=token_type_ids, use_cache=True)
        outputs_use_cache_conf = model(input_ids, token_type_ids=token_type_ids)
        outputs_no_past = model(input_ids, token_type_ids=token_type_ids, use_cache=False)

        self.parent.assertTrue(len(outputs) == len(outputs_use_cache_conf))
        self.parent.assertTrue(len(outputs) == len(outputs_no_past) + 1)

        output, past = outputs.to_tuple()

        # create hypothetical next token and extent to next_input_ids
        next_tokens = ids_tensor((self.batch_size, 1), config.vocab_size)
        next_token_types = ids_tensor([self.batch_size, 1], self.type_vocab_size)

        # append to next input_ids and token_type_ids
        next_input_ids = torch.cat([input_ids, next_tokens], dim=-1)
        next_token_type_ids = torch.cat([token_type_ids, next_token_types], dim=-1)

        output_from_no_past = model(next_input_ids, token_type_ids=next_token_type_ids)["last_hidden_state"]
        output_from_past = model(next_tokens, token_type_ids=next_token_types, past_key_values=past)[
            "last_hidden_state"
        ]

        # select random slice
        random_slice_idx = ids_tensor((1,), output_from_past.shape[-1]).item()
        output_from_no_past_slice = output_from_no_past[:, -1, random_slice_idx].detach()
        output_from_past_slice = output_from_past[:, 0, random_slice_idx].detach()

        # test that outputs are equal for slice
        self.parent.assertTrue(torch.allclose(output_from_past_slice, output_from_no_past_slice, atol=1e-3))

    def create_and_check_gpt_bigcode_model_attention_mask_past(
        self, config, input_ids, input_mask, head_mask, token_type_ids, *args
    ):
        model = GPTBigCodeModel(config=config)
        model.to(torch_device)
        model.eval()

        # create attention mask
        attn_mask = torch.ones(input_ids.shape, dtype=torch.long, device=torch_device)
        half_seq_length = self.seq_length // 2
        attn_mask[:, half_seq_length:] = 0

        # first forward pass
        output, past = model(input_ids, attention_mask=attn_mask).to_tuple()

        # create hypothetical next token and extent to next_input_ids
        next_tokens = ids_tensor((self.batch_size, 1), config.vocab_size)

        # change a random masked slice from input_ids
        random_seq_idx_to_change = ids_tensor((1,), half_seq_length).item() + 1
        random_other_next_tokens = ids_tensor((self.batch_size, 1), config.vocab_size).squeeze(-1)
        input_ids[:, -random_seq_idx_to_change] = random_other_next_tokens

        # append to next input_ids and attn_mask
        next_input_ids = torch.cat([input_ids, next_tokens], dim=-1)
        attn_mask = torch.cat(
            [attn_mask, torch.ones((attn_mask.shape[0], 1), dtype=torch.long, device=torch_device)],
            dim=1,
        )

        # get two different outputs
        output_from_no_past = model(next_input_ids, attention_mask=attn_mask)["last_hidden_state"]
        output_from_past = model(next_tokens, past_key_values=past, attention_mask=attn_mask)["last_hidden_state"]

        # select random slice
        random_slice_idx = ids_tensor((1,), output_from_past.shape[-1]).item()
        output_from_no_past_slice = output_from_no_past[:, -1, random_slice_idx].detach()
        output_from_past_slice = output_from_past[:, 0, random_slice_idx].detach()

        # test that outputs are equal for slice
        self.parent.assertTrue(torch.allclose(output_from_past_slice, output_from_no_past_slice, atol=1e-3))

    def create_and_check_gpt_bigcode_model_past_large_inputs(
        self, config, input_ids, input_mask, head_mask, token_type_ids, *args
    ):
        model = GPTBigCodeModel(config=config)
        model.to(torch_device)
        model.eval()

        # first forward pass
        outputs = model(input_ids, token_type_ids=token_type_ids, attention_mask=input_mask, use_cache=True)

        output, past = outputs.to_tuple()

        # create hypothetical next token and extent to next_input_ids
        next_tokens = ids_tensor((self.batch_size, 3), config.vocab_size)
        next_token_types = ids_tensor([self.batch_size, 3], self.type_vocab_size)
        next_mask = ids_tensor((self.batch_size, 3), vocab_size=2)

        # append to next input_ids and token_type_ids
        next_input_ids = torch.cat([input_ids, next_tokens], dim=-1)
        next_token_type_ids = torch.cat([token_type_ids, next_token_types], dim=-1)
        next_attention_mask = torch.cat([input_mask, next_mask], dim=-1)

        output_from_no_past = model(
            next_input_ids, token_type_ids=next_token_type_ids, attention_mask=next_attention_mask
        )["last_hidden_state"]
        output_from_past = model(
            next_tokens, token_type_ids=next_token_types, attention_mask=next_attention_mask, past_key_values=past
        )["last_hidden_state"]
        self.parent.assertTrue(output_from_past.shape[1] == next_tokens.shape[1])

        # select random slice
        random_slice_idx = ids_tensor((1,), output_from_past.shape[-1]).item()
        output_from_no_past_slice = output_from_no_past[:, -3:, random_slice_idx].detach()
        output_from_past_slice = output_from_past[:, :, random_slice_idx].detach()

        # test that outputs are equal for slice
        self.parent.assertTrue(torch.allclose(output_from_past_slice, output_from_no_past_slice, atol=1e-3))

    def create_and_check_lm_head_model(self, config, input_ids, input_mask, head_mask, token_type_ids, *args):
<<<<<<< HEAD
        model = GPTBigCodeLMHeadModel(config)
=======
        model = GPTBigCodeForCausalLM(config)
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
        model.to(torch_device)
        model.eval()

        result = model(input_ids, token_type_ids=token_type_ids, labels=input_ids)
        self.parent.assertEqual(result.loss.shape, ())
        self.parent.assertEqual(result.logits.shape, (self.batch_size, self.seq_length, self.vocab_size))

    def create_and_check_forward_and_backwards(
        self, config, input_ids, input_mask, head_mask, token_type_ids, *args, gradient_checkpointing=False
    ):
<<<<<<< HEAD
        model = GPTBigCodeLMHeadModel(config)
=======
        model = GPTBigCodeForCausalLM(config)
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
        model.to(torch_device)
        if gradient_checkpointing:
            model.gradient_checkpointing_enable()

        result = model(input_ids, token_type_ids=token_type_ids, labels=input_ids)
        self.parent.assertEqual(result.loss.shape, ())
        self.parent.assertEqual(result.logits.shape, (self.batch_size, self.seq_length, self.vocab_size))
        result.loss.backward()

<<<<<<< HEAD
    def create_and_check_double_lm_head_model(
        self, config, input_ids, input_mask, head_mask, token_type_ids, mc_token_ids, *args
    ):
        model = GPTBigCodeDoubleHeadsModel(config)
        model.to(torch_device)
        model.eval()

        multiple_choice_inputs_ids = input_ids.unsqueeze(1).expand(-1, self.num_choices, -1).contiguous()
        multiple_choice_input_mask = input_mask.unsqueeze(1).expand(-1, self.num_choices, -1).contiguous()
        multiple_choice_token_type_ids = token_type_ids.unsqueeze(1).expand(-1, self.num_choices, -1).contiguous()

        inputs = {
            "input_ids": multiple_choice_inputs_ids,
            "mc_token_ids": mc_token_ids,
            "attention_mask": multiple_choice_input_mask,
            "token_type_ids": multiple_choice_token_type_ids,
            "labels": multiple_choice_inputs_ids,
        }

        result = model(**inputs)
        self.parent.assertEqual(result.loss.shape, ())
        self.parent.assertEqual(
            result.logits.shape, (self.batch_size, self.num_choices, self.seq_length, self.vocab_size)
        )
        self.parent.assertEqual(result.mc_logits.shape, (self.batch_size, self.num_choices))

=======
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
    def create_and_check_gpt_bigcode_for_sequence_classification(
        self, config, input_ids, input_mask, head_mask, token_type_ids, mc_token_ids, sequence_labels, *args
    ):
        config.num_labels = self.num_labels
        model = GPTBigCodeForSequenceClassification(config)
        model.to(torch_device)
        model.eval()
        result = model(input_ids, attention_mask=input_mask, token_type_ids=token_type_ids, labels=sequence_labels)
        self.parent.assertEqual(result.logits.shape, (self.batch_size, self.num_labels))

    def create_and_check_gpt_bigcode_for_token_classification(
        self, config, input_ids, input_mask, head_mask, token_type_ids, mc_token_ids, sequence_labels, *args
    ):
        config.num_labels = self.num_labels
        model = GPTBigCodeForTokenClassification(config)
        model.to(torch_device)
        model.eval()
        result = model(input_ids, attention_mask=input_mask, token_type_ids=token_type_ids)
        self.parent.assertEqual(result.logits.shape, (self.batch_size, self.seq_length, self.num_labels))

    def create_and_check_gpt_bigcode_weight_initialization(self, config, *args):
        model = GPTBigCodeModel(config)
        model_std = model.config.initializer_range / math.sqrt(2 * model.config.n_layer)
        for key in model.state_dict().keys():
            if "c_proj" in key and "weight" in key:
                self.parent.assertLessEqual(abs(torch.std(model.state_dict()[key]) - model_std), 0.001)
                self.parent.assertLessEqual(abs(torch.mean(model.state_dict()[key]) - 0.0), 0.01)

    def prepare_config_and_inputs_for_common(self):
        config_and_inputs = self.prepare_config_and_inputs()

        (
            config,
            input_ids,
            input_mask,
            head_mask,
            token_type_ids,
            mc_token_ids,
            sequence_labels,
            token_labels,
            choice_labels,
        ) = config_and_inputs

        inputs_dict = {
            "input_ids": input_ids,
            "token_type_ids": token_type_ids,
            "head_mask": head_mask,
        }

        return config, inputs_dict


@require_torch
<<<<<<< HEAD
class GPTBigCodeModelTest(ModelTesterMixin, GenerationTesterMixin, unittest.TestCase):
    # TODO: Update the tests to use valid pretrained models.

    all_model_classes = (
        (
            GPTBigCodeModel,
            GPTBigCodeLMHeadModel,
            GPTBigCodeDoubleHeadsModel,
=======
class GPTBigCodeMQAModelTest(ModelTesterMixin, GenerationTesterMixin, PipelineTesterMixin, unittest.TestCase):
    # TODO: Update the tests to use valid pretrained models.
    all_model_classes = (
        (
            GPTBigCodeModel,
            GPTBigCodeForCausalLM,
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
            GPTBigCodeForSequenceClassification,
            GPTBigCodeForTokenClassification,
        )
        if is_torch_available()
        else ()
    )
<<<<<<< HEAD
    all_generative_model_classes = (GPTBigCodeLMHeadModel, GPTBigCodeDoubleHeadsModel) if is_torch_available() else ()
    all_parallelizable_model_classes = (
        (GPTBigCodeLMHeadModel, GPTBigCodeDoubleHeadsModel) if is_torch_available() else ()
    )
    fx_compatible = True
    test_missing_keys = False
    test_model_parallel = True
=======
    all_generative_model_classes = (GPTBigCodeForCausalLM,) if is_torch_available() else ()
    fx_compatible = False
    test_missing_keys = False
    test_pruning = False
    test_torchscript = False
    multi_query = True
    pipeline_model_mapping = (
        {
            "feature-extraction": GPTBigCodeModel,
            "text-classification": GPTBigCodeForSequenceClassification,
            "text-generation": GPTBigCodeForCausalLM,
            "token-classification": GPTBigCodeForTokenClassification,
            "zero-shot": GPTBigCodeForSequenceClassification,
        }
        if is_torch_available()
        else {}
    )
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465

    # special case for DoubleHeads model
    def _prepare_for_class(self, inputs_dict, model_class, return_labels=False):
        inputs_dict = super()._prepare_for_class(inputs_dict, model_class, return_labels=return_labels)

<<<<<<< HEAD
        if return_labels:
            if model_class.__name__ == "GPTBigCodeDoubleHeadsModel":
                inputs_dict["labels"] = torch.zeros(
                    (self.model_tester.batch_size, self.model_tester.num_choices, self.model_tester.seq_length),
                    dtype=torch.long,
                    device=torch_device,
                )
                inputs_dict["input_ids"] = inputs_dict["labels"]
                inputs_dict["token_type_ids"] = inputs_dict["labels"]
                inputs_dict["mc_token_ids"] = torch.zeros(
                    (self.model_tester.batch_size, self.model_tester.num_choices),
                    dtype=torch.long,
                    device=torch_device,
                )
                inputs_dict["mc_labels"] = torch.zeros(
                    self.model_tester.batch_size, dtype=torch.long, device=torch_device
                )
        return inputs_dict

    def setUp(self):
        self.model_tester = GPTBigCodeModelTester(self)
        self.config_tester = ConfigTester(self, config_class=GPTBigCodeConfig, n_embd=37)

    def test_config(self):
        self.config_tester.run_common_tests()

=======
        return inputs_dict

    def setUp(self):
        self.model_tester = GPTBigCodeModelTester(self, multi_query=self.multi_query)
        self.config_tester = ConfigTester(self, config_class=GPTBigCodeConfig, n_embd=37)

    def tearDown(self):
        import gc

        gc.collect()

    def test_config(self):
        self.config_tester.run_common_tests()

    @unittest.skip("MQA models does not support retain_grad")
    def test_retain_grad_hidden_states_attentions(self):
        pass

    @unittest.skip("Contrastive search not supported due to non-standard caching mechanism")
    def test_contrastive_generate(self):
        pass

    @unittest.skip("Contrastive search not supported due to non-standard caching mechanism")
    def test_contrastive_generate_dict_outputs_use_cache(self):
        pass

    @unittest.skip("CPU offload seems to be broken for some reason - tiny models keep hitting corner cases")
    def test_cpu_offload(self):
        pass

    @unittest.skip("Disk offload seems to be broken for some reason - tiny models keep hitting corner cases")
    def test_disk_offload(self):
        pass

>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
    def test_gpt_bigcode_model(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_gpt_bigcode_model(*config_and_inputs)

    def test_gpt_bigcode_model_past(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_gpt_bigcode_model_past(*config_and_inputs)

    def test_gpt_bigcode_model_att_mask_past(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_gpt_bigcode_model_attention_mask_past(*config_and_inputs)

    def test_gpt_bigcode_model_past_large_inputs(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_gpt_bigcode_model_past_large_inputs(*config_and_inputs)

    def test_gpt_bigcode_lm_head_model(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_lm_head_model(*config_and_inputs)

<<<<<<< HEAD
    def test_gpt_bigcode_double_lm_head_model(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_double_lm_head_model(*config_and_inputs)

=======
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
    def test_gpt_bigcode_sequence_classification_model(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_gpt_bigcode_for_sequence_classification(*config_and_inputs)

    def test_gpt_bigcode_token_classification_model(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_gpt_bigcode_for_token_classification(*config_and_inputs)

    def test_gpt_bigcode_gradient_checkpointing(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_forward_and_backwards(*config_and_inputs, gradient_checkpointing=True)

    def test_gpt_bigcode_scale_attn_by_inverse_layer_idx(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs(scale_attn_by_inverse_layer_idx=True)
        self.model_tester.create_and_check_forward_and_backwards(*config_and_inputs)

    def test_gpt_bigcode_reorder_and_upcast_attn(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs(reorder_and_upcast_attn=True)
        self.model_tester.create_and_check_forward_and_backwards(*config_and_inputs)

    def test_gpt_bigcode_weight_initialization(self):
        config_and_inputs = self.model_tester.prepare_config_and_inputs()
        self.model_tester.create_and_check_gpt_bigcode_weight_initialization(*config_and_inputs)

<<<<<<< HEAD
    @slow
    def test_batch_generation(self):
        model = GPTBigCodeLMHeadModel.from_pretrained("bigcode/santacoder-fast-inference")
        model.to(torch_device)
        tokenizer = GPT2Tokenizer.from_pretrained("bigcode/santacoder")

        tokenizer.padding_side = "left"

        # Define PAD Token = EOS Token = 50256
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id

        # use different length sentences to test batching
        sentences = [
            "Hello, my dog is a little",
            "Today, I",
        ]

        inputs = tokenizer(sentences, return_tensors="pt", padding=True)
        input_ids = inputs["input_ids"].to(torch_device)
        token_type_ids = torch.cat(
            [
                input_ids.new_full((input_ids.shape[0], input_ids.shape[1] - 1), 0),
                input_ids.new_full((input_ids.shape[0], 1), 500),
            ],
            dim=-1,
        )

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=inputs["attention_mask"].to(torch_device),
        )

        outputs_tt = model.generate(
            input_ids=input_ids,
            attention_mask=inputs["attention_mask"].to(torch_device),
            token_type_ids=token_type_ids,
        )

        inputs_non_padded = tokenizer(sentences[0], return_tensors="pt").input_ids.to(torch_device)
        output_non_padded = model.generate(input_ids=inputs_non_padded)

        num_paddings = inputs_non_padded.shape[-1] - inputs["attention_mask"][-1].long().sum().cpu().item()
        inputs_padded = tokenizer(sentences[1], return_tensors="pt").input_ids.to(torch_device)
        output_padded = model.generate(input_ids=inputs_padded, max_length=model.config.max_length - num_paddings)

        batch_out_sentence = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        batch_out_sentence_tt = tokenizer.batch_decode(outputs_tt, skip_special_tokens=True)
        non_padded_sentence = tokenizer.decode(output_non_padded[0], skip_special_tokens=True)
        padded_sentence = tokenizer.decode(output_padded[0], skip_special_tokens=True)

        expected_output_sentence = [
            "Hello, my dog is a little bit of a mess. I'm not sure if he's going",
            "Today, I'm going to be doing a lot of research on this. I",
        ]
        self.assertListEqual(expected_output_sentence, batch_out_sentence)
        self.assertTrue(batch_out_sentence_tt != batch_out_sentence)  # token_type_ids should change output
        self.assertListEqual(expected_output_sentence, [non_padded_sentence, padded_sentence])

    @slow
    def test_batch_generation_2heads(self):
        model = GPTBigCodeDoubleHeadsModel.from_pretrained("bigcode/santacoder-fast-inference")
        model.to(torch_device)
        tokenizer = GPT2Tokenizer.from_pretrained("bigcode/santacoder")

        tokenizer.padding_side = "left"

        # This tokenizer has no pad token, so we have to set it in some way
        # Define PAD Token = EOS Token = 50256
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id

        # use different length sentences to test batching
        sentences = [
            "Hello, my dog is a little",
            "Today, I",
        ]

        inputs = tokenizer(sentences, return_tensors="pt", padding=True)
        input_ids = inputs["input_ids"].to(torch_device)
        token_type_ids = torch.cat(
            [
                input_ids.new_full((input_ids.shape[0], input_ids.shape[1] - 1), 0),
                input_ids.new_full((input_ids.shape[0], 1), 500),
            ],
            dim=-1,
        )

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=inputs["attention_mask"].to(torch_device),
        )

        outputs_tt = model.generate(
            input_ids=input_ids,
            attention_mask=inputs["attention_mask"].to(torch_device),
            token_type_ids=token_type_ids,
        )

        inputs_non_padded = tokenizer(sentences[0], return_tensors="pt").input_ids.to(torch_device)
        output_non_padded = model.generate(input_ids=inputs_non_padded)

        num_paddings = inputs_non_padded.shape[-1] - inputs["attention_mask"][-1].long().sum().cpu().item()
        inputs_padded = tokenizer(sentences[1], return_tensors="pt").input_ids.to(torch_device)
        output_padded = model.generate(input_ids=inputs_padded, max_length=model.config.max_length - num_paddings)

        batch_out_sentence = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        batch_out_sentence_tt = tokenizer.batch_decode(outputs_tt, skip_special_tokens=True)
        non_padded_sentence = tokenizer.decode(output_non_padded[0], skip_special_tokens=True)
        padded_sentence = tokenizer.decode(output_padded[0], skip_special_tokens=True)

        expected_output_sentence = [
            "Hello, my dog is a little bit of a mess. I'm not sure if he's going",
            "Today, I'm going to be doing a lot of research on this. I",
        ]
        self.assertListEqual(expected_output_sentence, batch_out_sentence)
        self.assertTrue(batch_out_sentence_tt != batch_out_sentence)  # token_type_ids should change output
        self.assertListEqual(expected_output_sentence, [non_padded_sentence, padded_sentence])

    @slow
    def test_model_from_pretrained(self):
        for model_name in GPT_BIGCODE_PRETRAINED_MODEL_ARCHIVE_LIST[:1]:
            model = GPTBigCodeModel.from_pretrained(model_name)
            self.assertIsNotNone(model)


@require_torch
class GPTBigCodeModelLanguageGenerationTest(unittest.TestCase):
    def _test_lm_generate_gpt_bigcode_helper(
        self,
        gradient_checkpointing=False,
        reorder_and_upcast_attn=False,
        scale_attn_by_inverse_layer_idx=False,
        verify_outputs=True,
    ):
        model = GPTBigCodeLMHeadModel.from_pretrained(
            "bigcode/santacoder-fast-inference",
            reorder_and_upcast_attn=reorder_and_upcast_attn,
            scale_attn_by_inverse_layer_idx=scale_attn_by_inverse_layer_idx,
        )
        if gradient_checkpointing:
            model.gradient_checkpointing_enable()
        else:
            model.gradient_checkpointing_disable()
        model.to(torch_device)

        # The dog
        input_ids = torch.tensor([[464, 3290]], dtype=torch.long, device=torch_device)

        # The dog was found in a field near the intersection of West and West Streets.\n\nThe dog
        # fmt: off
        expected_output_ids = [
            464, 3290, 373, 1043, 287, 257, 2214, 1474, 262, 16246, 286, 2688, 290, 2688, 27262, 13, 198, 198, 464, 3290,
        ]
        # fmt: on
        output_ids = model.generate(input_ids, do_sample=False)
        if verify_outputs:
            self.assertListEqual(output_ids[0].tolist(), expected_output_ids)

    @slow
    def test_lm_generate_gpt_bigcode(self):
        self._test_lm_generate_gpt_bigcode_helper()

    @slow
    def test_lm_generate_gpt_bigcode_with_gradient_checkpointing(self):
        self._test_lm_generate_gpt_bigcode_helper(gradient_checkpointing=True)

    @slow
    def test_lm_generate_gpt_bigcode_with_reorder_and_upcast_attn(self):
        self._test_lm_generate_gpt_bigcode_helper(reorder_and_upcast_attn=True)

    @slow
    def test_lm_generate_gpt_bigcode_with_scale_attn_by_inverse_layer_idx(self):
        self._test_lm_generate_gpt_bigcode_helper(scale_attn_by_inverse_layer_idx=True, verify_outputs=False)

    @slow
    def test_gpt_bigcode_sample(self):
        tokenizer = GPT2Tokenizer.from_pretrained("bigcode/santacoder")
        model = GPTBigCodeLMHeadModel.from_pretrained("bigcode/santacoder-fast-inference")
        model.to(torch_device)

        torch.manual_seed(0)
        tokenized = tokenizer("Today is a nice day and", return_tensors="pt", return_token_type_ids=True)
        input_ids = tokenized.input_ids.to(torch_device)
        output_ids = model.generate(input_ids, do_sample=True)
        output_str = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        token_type_ids = tokenized.token_type_ids.to(torch_device)
        output_seq = model.generate(input_ids=input_ids, do_sample=True, num_return_sequences=5)
        output_seq_tt = model.generate(
            input_ids=input_ids, token_type_ids=token_type_ids, do_sample=True, num_return_sequences=5
        )
        output_seq_strs = tokenizer.batch_decode(output_seq, skip_special_tokens=True)
        output_seq_tt_strs = tokenizer.batch_decode(output_seq_tt, skip_special_tokens=True)

        EXPECTED_OUTPUT_STR = (
            "Today is a nice day and if you don't know anything about the state of play during your holiday"
        )
        self.assertEqual(output_str, EXPECTED_OUTPUT_STR)
        self.assertTrue(
            all([output_seq_strs[idx] != output_seq_tt_strs[idx] for idx in range(len(output_seq_tt_strs))])
        )  # token_type_ids should change output

    @slow
    def test_gpt_bigcode_sample_max_time(self):
        tokenizer = GPT2Tokenizer.from_pretrained("bigcode/santacoder")
        model = GPTBigCodeLMHeadModel.from_pretrained("bigcode/santacoder-fast-inference")
        model.to(torch_device)

        torch.manual_seed(0)
        tokenized = tokenizer("Today is a nice day and", return_tensors="pt", return_token_type_ids=True)
        input_ids = tokenized.input_ids.to(torch_device)

        MAX_TIME = 0.5

        start = datetime.datetime.now()
        model.generate(input_ids, do_sample=True, max_time=MAX_TIME, max_length=256)
        duration = datetime.datetime.now() - start
        self.assertGreater(duration, datetime.timedelta(seconds=MAX_TIME))
        self.assertLess(duration, datetime.timedelta(seconds=1.5 * MAX_TIME))

        start = datetime.datetime.now()
        model.generate(input_ids, do_sample=False, max_time=MAX_TIME, max_length=256)
        duration = datetime.datetime.now() - start
        self.assertGreater(duration, datetime.timedelta(seconds=MAX_TIME))
        self.assertLess(duration, datetime.timedelta(seconds=1.5 * MAX_TIME))

        start = datetime.datetime.now()
        model.generate(input_ids, do_sample=False, num_beams=2, max_time=MAX_TIME, max_length=256)
        duration = datetime.datetime.now() - start
        self.assertGreater(duration, datetime.timedelta(seconds=MAX_TIME))
        self.assertLess(duration, datetime.timedelta(seconds=1.5 * MAX_TIME))

        start = datetime.datetime.now()
        model.generate(input_ids, do_sample=True, num_beams=2, max_time=MAX_TIME, max_length=256)
        duration = datetime.datetime.now() - start
        self.assertGreater(duration, datetime.timedelta(seconds=MAX_TIME))
        self.assertLess(duration, datetime.timedelta(seconds=1.5 * MAX_TIME))

        start = datetime.datetime.now()
        model.generate(input_ids, do_sample=False, max_time=None, max_length=256)
        duration = datetime.datetime.now() - start
        self.assertGreater(duration, datetime.timedelta(seconds=1.5 * MAX_TIME))

    @slow
    def test_contrastive_search_gpt_bigcode(self):
        article = (
            "DeepMind Technologies is a British artificial intelligence subsidiary of Alphabet Inc. and research "
            "laboratory founded in 2010. DeepMind was acquired by Google in 2014. The company is based"
        )

        gpt_bigcode_tokenizer = GPT2Tokenizer.from_pretrained("bigcode/santacoder")
        gpt_bigcode_model = GPTBigCodeLMHeadModel.from_pretrained("bigcode/santacoder-fast-inference").to(torch_device)
        input_ids = gpt_bigcode_tokenizer(article, return_tensors="pt").input_ids.to(torch_device)

        outputs = gpt_bigcode_model.generate(input_ids, penalty_alpha=0.6, top_k=4, max_length=256)

        generated_text = gpt_bigcode_tokenizer.batch_decode(outputs, skip_special_tokens=True)

        self.assertListEqual(
            generated_text,
            [
                "DeepMind Technologies is a British artificial intelligence subsidiary of Alphabet Inc. and research "
                "laboratory founded in 2010. DeepMind was acquired by Google in 2014. The company is based in London, "
                "United Kingdom\n\nGoogle has a lot of data on its users and uses it to improve its products, such as "
                "Google Now, which helps users find the information they're looking for on the web. But the company "
                "is not the only one to collect data on its users. Facebook, for example, has its own facial "
                "recognition technology, as well as a database of millions of photos that it uses to personalize its "
                "News Feed.\n\nFacebook's use of data is a hot topic in the tech industry, with privacy advocates "
                "concerned about the company's ability to keep users' information private. In a blog post last "
                'year, Facebook CEO Mark Zuckerberg said his company would "do our best to be transparent about our '
                'data use and how we use it."\n\n"We have made it clear that we do not sell or share your data with '
                'third parties," Zuckerberg wrote. "If you have questions or concerns, please reach out to us at '
                'privacy@facebook.com."\n\nGoogle declined to comment on the privacy implications of its use of data, '
                "but said in a statement to The Associated Press that"
            ],
        )


@require_torch
class GPTBigCodeAttentionTest(unittest.TestCase):
    def get_attention(self, attention_type: AttentionType):
        config = GPTBigCodeConfig.from_pretrained(
            "bigcode/santacoder-fast-inference",
            attention_type=attention_type,
=======

@require_torch
class GPTBigCodeMHAModelTest(GPTBigCodeMQAModelTest):
    # `parameterized_class` breaks with mixins, so we use inheritance instead
    multi_query = False


@slow
@require_torch
class GPTBigCodeModelLanguageGenerationTest(unittest.TestCase):
    def test_generate_simple(self):
        model = GPTBigCodeForCausalLM.from_pretrained("bigcode/gpt_bigcode-santacoder").to(torch_device)
        tokenizer = GPT2TokenizerFast.from_pretrained("bigcode/gpt_bigcode-santacoder")

        input_ids = tokenizer("def print_hello_world():", return_tensors="pt").input_ids.to(torch_device)

        output_sequence = model.generate(input_ids)
        output_sentence = tokenizer.decode(output_sequence[0], skip_special_tokens=True)

        expected_output = """def print_hello_world():\n    print("Hello World!")\n\n\ndef print_hello_"""
        self.assertEqual(output_sentence, expected_output)

    def test_generate_batched(self):
        tokenizer = GPT2TokenizerFast.from_pretrained("bigcode/gpt_bigcode-santacoder")
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "left"

        model = GPTBigCodeForCausalLM.from_pretrained("bigcode/gpt_bigcode-santacoder").to(torch_device)

        inputs = tokenizer(["def print_hello_world():", "def say_hello():"], return_tensors="pt", padding=True).to(
            torch_device
        )
        outputs = model.generate(**inputs)
        outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        expected_output = [
            'def print_hello_world():\n    print("Hello World!")\n\n\ndef print_hello_',
            'def say_hello():\n    print("Hello, World!")\n\n\nsay_hello()',
        ]
        self.assertListEqual(outputs, expected_output)


@require_torch
class GPTBigCodeMQATest(unittest.TestCase):
    def get_attention(self, multi_query):
        config = GPTBigCodeConfig.from_pretrained(
            "bigcode/gpt_bigcode-santacoder",
            multi_query=multi_query,
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
            attn_pdrop=0,
            resid_pdrop=0,
        )
        return GPTBigCodeAttention(config)

    @parameterized.expand([(seed, is_train_mode) for seed in range(5) for is_train_mode in [True, False]])
<<<<<<< HEAD
    def test_mqa_correctness(self, seed, is_train_mode=True):
        torch.manual_seed(seed)
        embed_dim = 2048
        head_dim = 128

        # GET THE WEIGHTS FROM MULTI-QUERY ATTENTION 1
        attention_mq1 = self.get_attention(AttentionType.MULTI_QUERY_1)
        state_dict_mq1 = attention_mq1.state_dict()
        attn_weight, attn_k_weight, attn_v_weight = torch.split(
            state_dict_mq1["c_attn.weight"], [embed_dim, head_dim, head_dim], dim=1
        )
        attn_bias, attn_k_bias, attn_v_bias = torch.split(
            state_dict_mq1["c_attn.bias"], [embed_dim, head_dim, head_dim], dim=0
        )
        proj = state_dict_mq1["c_proj.weight"]
        proj_bias = state_dict_mq1["c_proj.bias"]

        # PUT THEM INTO THE MULTI-HEAD ATTENTION
        num_heads = 16
        c_attn_weight = torch.hstack([attn_weight] + num_heads * [attn_k_weight] + num_heads * [attn_v_weight])
        c_attn_bias = torch.hstack([attn_bias] + num_heads * [attn_k_bias] + num_heads * [attn_v_bias])
        attention_mh = self.get_attention(AttentionType.MULTI_HEAD)
        state_dict = attention_mh.state_dict()
        state_dict["c_attn.weight"] = c_attn_weight
        state_dict["c_attn.bias"] = c_attn_bias
        state_dict["c_proj.weight"] = proj
        state_dict["c_proj.bias"] = proj_bias
        attention_mh.load_state_dict(state_dict)

        # PUT THEM INTO THE MULTI-QUERY ATTENTION 2
        attention_mq2 = self.get_attention(AttentionType.MULTI_QUERY_2)
        state_dict_mq2 = attention_mq2.state_dict()
        state_dict_mq2["q_attn.weight"] = attn_weight
        state_dict_mq2["q_attn.bias"] = attn_bias
        state_dict_mq2["kv_attn.weight"] = torch.hstack([attn_k_weight, attn_v_weight])
        state_dict_mq2["kv_attn.bias"] = torch.hstack([attn_k_bias, attn_v_bias])
        state_dict_mq2["c_proj.weight"] = proj
        state_dict_mq2["c_proj.bias"] = proj_bias
        attention_mq2.load_state_dict(state_dict_mq2)

        # PUT THE MODEL INTO THE CORRECT MODE
        attention_mh.train(is_train_mode)
        attention_mq1.train(is_train_mode)
        attention_mq2.train(is_train_mode)
=======
    def test_mqa_reduces_to_mha(self, seed, is_train_mode=True):
        torch.manual_seed(seed)

        # CREATE MQA AND MHA ATTENTIONS
        attention_mqa = self.get_attention(True)
        attention_mha = self.get_attention(False)

        # ENFORCE MATCHING WEIGHTS
        num_heads = attention_mqa.num_heads
        embed_dim = attention_mqa.embed_dim
        head_dim = attention_mqa.head_dim

        with torch.no_grad():
            mqa_q_weight = attention_mqa.c_attn.weight[:embed_dim, :].view(num_heads, 1, head_dim, embed_dim)
            mqa_kv_weight = attention_mqa.c_attn.weight[embed_dim:, :].view(1, 2, head_dim, embed_dim)
            mha_c_weight = torch.cat(
                [mqa_q_weight, mqa_kv_weight.expand(num_heads, 2, head_dim, embed_dim)], dim=1
            ).view(3 * num_heads * head_dim, embed_dim)

            mqa_q_bias = attention_mqa.c_attn.bias[:embed_dim].view(num_heads, 1, head_dim)
            mqa_kv_bias = attention_mqa.c_attn.bias[embed_dim:].view(1, 2, head_dim)
            mha_c_bias = torch.cat([mqa_q_bias, mqa_kv_bias.expand(num_heads, 2, head_dim)], dim=1).view(
                3 * num_heads * head_dim
            )

            attention_mha.c_attn.weight.copy_(mha_c_weight)
            attention_mha.c_attn.bias.copy_(mha_c_bias)
            attention_mha.c_proj.weight.copy_(attention_mqa.c_proj.weight)
            attention_mha.c_proj.bias.copy_(attention_mqa.c_proj.bias)

        # PUT THE MODEL INTO THE CORRECT MODE
        attention_mha.train(is_train_mode)
        attention_mqa.train(is_train_mode)
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465

        # RUN AN INPUT THROUGH THE MODELS
        num_tokens = 5
        hidden_states = torch.randn(1, num_tokens, embed_dim)
<<<<<<< HEAD
        attention_mh_result = attention_mh(hidden_states)[0]
        attention_mq1_result = attention_mq1(hidden_states)[0]
        attention_mq2_result = attention_mq2(hidden_states)[0]

        # CHECK THAT ALL OUTPUTS ARE THE SAME
        tolerance = 1e-5
        self.assertTrue(torch.allclose(attention_mh_result, attention_mq1_result, atol=tolerance))
        self.assertTrue(torch.allclose(attention_mh_result, attention_mq2_result, atol=tolerance))
        self.assertTrue(torch.allclose(attention_mq1_result, attention_mq2_result, atol=tolerance))
=======
        attention_mha_result = attention_mha(hidden_states)[0]
        attention_mqa_result = attention_mqa(hidden_states)[0]

        # CHECK THAT ALL OUTPUTS ARE THE SAME
        self.assertTrue(torch.allclose(attention_mha_result, attention_mqa_result, atol=1e-5))
>>>>>>> e0921c6b53310a47b10f01633809b2b9f785a465
