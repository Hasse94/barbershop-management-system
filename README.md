# Barbershop Management System

A full-stack system for running a barbershop: managing barbers, services and appointments, tracking earnings, and letting customers book online.

## Features
- Add and remove barbers (soft delete — history is kept)
- Register customers
- Create appointments with one or more services
- Track appointment status: scheduled, completed, cancelled, no-show
- Calculate each barber's earnings (service revenue + tips)
- Manage available services and prices

### Roles
- **Owner** — manages barbers, services, and reports
- **Barber** — views and updates their own appointments
- **Customer** — books and manages their own appointments

## Tech Stack
- **Backend:** Python, FastAPI, Pydantic, SQLAlchemy, Alembic
- **Database:** PostgreSQL
- **Frontend:** React, TypeScript, Vite
- **Testing:** pytest
- **DevOps:** Docker, GitHub Actions, Render, Vercel

## Roadmap
- [ ] Phase 0 – Project setup and Git workflow
- [ ] Phase 1 – Domain model in pure Python (OOP)
- [ ] Phase 2 – Database with PostgreSQL and SQLAlchemy
- [ ] Phase 3 – REST API with FastAPI
- [ ] Phase 4 – Authentication and role-based access
- [ ] Phase 5 – Earnings reports and availability search
- [ ] Phase 6 – Frontend
- [ ] Phase 7 – Docker, CI/CD and deployment

## Status
🚧 In development — Phase 0