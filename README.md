# Barbershop Management System

A full-stack system for running a barbershop: managing barbers, services and appointments, tracking earnings, and letting customers book online.

I'm building it step by step to strengthen my backend skills, starting with object-oriented Python and working up to a database, a REST API and a frontend.

## Features
- Add and remove barbers (removed barbers keep their history)
- Register customers
- Create appointments with one or more services
- Track appointment status: scheduled, completed, cancelled, no-show
- Calculate each barber's earnings, including tips
- Manage available services and prices

### Roles
- **Owner:** manages barbers, services and reports
- **Barber:** sees and updates their own appointments
- **Customer:** books and manages their own appointments

## Tech Stack
- **Backend:** Python, FastAPI, Pydantic, SQLAlchemy, Alembic
- **Database:** PostgreSQL
- **Frontend:** React, TypeScript, Vite
- **Testing:** pytest
- **DevOps:** Docker, GitHub Actions, Render, Vercel

## Running it locally
```bash
git clone https://github.com/Hasse94/barbershop-management-system.git
cd barbershop-management-system
python -m venv .venv
.venv\Scripts\Activate.ps1        # Mac/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

## Roadmap
- [x] Phase 0 – Project setup and Git workflow
- [ ] Phase 1 – Domain model in pure Python (OOP)
  - [x] Service
  - [ ] Barber and Customer
  - [ ] Appointment
  - [ ] BarberShop
- [ ] Phase 2 – Database with PostgreSQL and SQLAlchemy
- [ ] Phase 3 – REST API with FastAPI
- [ ] Phase 4 – Authentication and role-based access
- [ ] Phase 5 – Earnings reports and availability search
- [ ] Phase 6 – Frontend
- [ ] Phase 7 – Docker, CI/CD and deployment

## Status
🚧 Working on Phase 1. The Service class is done and tested, Barber and Customer are next.