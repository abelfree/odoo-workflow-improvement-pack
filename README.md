# Odoo Workflow Improvement Pack

[![Odoo](https://img.shields.io/badge/Odoo-16%2B-5E2750)](https://www.odoo.com/)
[![License: LGPL-3.0](https://img.shields.io/badge/License-LGPL--3.0-blue.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Portfolio_Ready-brightgreen)](#)
[![Last Commit](https://img.shields.io/github/last-commit/abelfree/odoo-workflow-improvement-pack)](https://github.com/abelfree/odoo-workflow-improvement-pack/commits/master)


## Problem
Operations teams often spend extra clicks and time in core sales workflows, while weak validation allows avoidable user errors that later become support tickets.

## Solution
This project combines backend validation and frontend view enhancement to shorten the operator path and reduce invalid transactions.

## What It Demonstrates
- Backend constraint to block zero/negative sale line quantities
- Form view extension with quick confirm action
- Demo and metrics templates for before/after comparison

## Architecture
- `addons/workflow_improvement_pack/models/sale_order.py`
- `addons/workflow_improvement_pack/views/sale_order_views.xml`
- `assets/demo_notes.md`
- `docs/impact_metrics.md`

## Demo Flow
1. Install addon with Sales and Stock dependencies.
2. Create sales orders with edge-case line quantities.
3. Validate backend constraint behavior and quick confirm UI.
4. Record cycle-time improvements in `docs/impact_metrics.md`.

## Portfolio Talking Points
- Balancing strict validation with user productivity.
- Communicating UI improvements using measurable outcomes.
- Full-stack approach to ERP workflow optimization.



