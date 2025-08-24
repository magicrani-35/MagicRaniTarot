# Tarot Trail - A Spiritual Adventure Game (Sandbox-Compatible Version)

# Player Stats
data = {
    "name": "Amara",  # Mocked soul name to avoid input()
    "energy": 100,
    "clarity": 100,
    "alignment": 100,
    "location": "Fool's Meadow",
    "inventory": []
}

# Function to update stats
def update_stat(stat, change):
    data[stat] += change
    if data[stat] < 0:
        data[stat] = 0
    elif data[stat] > 100:
        data[stat] = 100

# Function to display stats
def show_stats():
    print("\n💫 Your Current Stats 💫")
    print(f"Energy: {data['energy']}")
    print(f"Clarity: {data['clarity']}")
    print(f"Alignment: {data['alignment']}")
    print(f"Inventory: {', '.join(data['inventory']) if data['inventory'] else 'None'}")

# Function to simulate tarot pull
def draw_tarot():
    import random
    cards = ["The Magician", "The Empress", "Strength", "Justice", "The Moon", "The Sun", "Judgment"]
    return random.choice(cards)

# Introduction
print("\U0001F52E Welcome to The Tarot Trail \U0001F52E")
print("You are The Seeker, journeying toward the Sacred Temple of Inner Truth.")
print(f"\nBlessings, {data['name']}. Your journey begins at {data['location']}.")

# Scene 1: The Fool's Meadow
print("\n🃏 A card appears before you... It is The Fool.")
print("Do you:")
print("1. Step forward into the unknown")
print("2. Retreat and wait for a sign")
choice = "1"
if choice == "1":
    print("\nYou step boldly forward. A breeze carries your fears away.")
    update_stat("alignment", 10)
    data['location'] = "High Priestess's Pool"
elif choice == "2":
    print("\nYou wait... but the moment passes. Doubt creeps in.")
    update_stat("clarity", -10)
else:
    print("\nThe spirits do not understand your choice. Confusion surrounds you.")
    update_stat("clarity", -5)
show_stats()

# Scene 2: High Priestess's Pool
print(f"\n{data['name']}, you arrive at the High Priestess’s Pool. The waters shimmer with moonlight.")
print("\n🃏 A card floats on the surface... It is The High Priestess.")
print("She whispers: 'Not all answers are meant to be spoken. Trust what you feel.'")
print("Do you:")
print("1. Meditate beside the pool and listen for inner guidance.")
print("2. Ask the Priestess to reveal your next step.")
print("3. Ignore the moment and move on quickly.")
tarot_choice = "1"
if tarot_choice == "1":
    print("\nYou hear a whisper in the breeze... a forgotten truth awakens in your soul.")
    update_stat("clarity", 15)
    data['inventory'].append("Moonstone")
elif tarot_choice == "2":
    print("\nShe smiles but says nothing. The lesson is silence. You feel unsettled.")
    update_stat("alignment", -5)
elif tarot_choice == "3":
    print("\nYou rush past. The waters ripple behind you, disturbed.")
    update_stat("energy", -10)
else:
    print("\nThe moment dissolves in mist. Confusion lingers.")
    update_stat("clarity", -5)
show_stats()

# Scene 3: The Tower of Illusions
print(f"\n{data['name']}, you now face the Tower of Illusions. Shadows flicker across its mirrored walls.")
print("\n🃏 A card appears in the air... It is The Tower.")
print("A voice bellows: 'Will you destroy the illusion, or be destroyed by it?'")
print("Do you:")
print("1. Break the mirror and face what lies behind.")
print("2. Turn away and pretend it isn’t there.")
print("3. Ask your Inner Child for help.")
tower_choice = "3"
if tower_choice == "1":
    print("\nThe mirror shatters. You see your true reflection. It is painful but freeing.")
    update_stat("alignment", 10)
    update_stat("energy", -10)
elif tower_choice == "2":
    print("\nYou turn your back, but the Tower follows you. The illusion deepens.")
    update_stat("clarity", -15)
elif tower_choice == "3":
    print("\nA gentle voice within says, 'I’m still here.' You smile through tears.")
    update_stat("clarity", 10)
    update_stat("alignment", 5)
    data['inventory'].append("Mirror Fragment")
else:
    print("\nThe tower shifts and reshapes. Confusion takes root.")
    update_stat("energy", -5)
show_stats()

# Scene 4: Death's Crossing
print(f"\n{data['name']}, you arrive at Death's Crossing — a silent valley cloaked in mist.")
print("A skeletal figure in a dark cloak stands beside a black river.")
print("\n🃏 A card appears in the air... It is Death.")
print("He whispers: 'You cannot carry everything. What will you leave behind?'")
print("Do you:")
print("1. Burn a painful memory to light your path.")
print("2. Let go of a false belief you've clung to.")
print("3. Refuse to give anything up and move forward heavier.")
death_choice = "2"
if death_choice == "1":
    print("\nYou set the memory aflame. The path ahead glows briefly, then clears.")
    update_stat("energy", 10)
    update_stat("clarity", 5)
elif death_choice == "2":
    print("\nYou whisper a truth to the mist and release the belief. A weight lifts.")
    update_stat("alignment", 15)
elif death_choice == "3":
    print("\nYou march forward, burdened. The crossing is slow and draining.")
    update_stat("energy", -15)
    update_stat("clarity", -10)
else:
    print("\nThe ferryman waits silently. Nothing changes until you choose.")
    update_stat("clarity", -5)
show_stats()

# Scene 5: The Star's Ascent
print(f"\n{data['name']}, night falls as you climb a glowing hillside — this is The Star’s Ascent.")
print("The sky is clear, and countless stars shimmer like blessings above.")
print("\n🃏 A card floats in the starlight... It is The Star.")
print("A voice sings: 'Hope is not naive. It is sacred. Will you receive it?'")
print("Do you:")
print("1. Make a wish and trust it will come to be.")
print("2. Rest under the stars and reflect.")
print("3. Ignore the stars and keep climbing without pause.")
star_choice = "1"
if star_choice == "1":
    print("\nA warm glow surrounds you. You feel held by the universe.")
    update_stat("clarity", 10)
    update_stat("alignment", 10)
    data['inventory'].append("Star Dust")
elif star_choice == "2":
    print("\nYou sleep peacefully, dreams full of light. You awaken renewed.")
    update_stat("energy", 10)
elif star_choice == "3":
    print("\nYou push forward, but exhaustion grows. The stars fade behind you.")
    update_stat("energy", -10)
else:
    print("\nThe stars flicker uncertainly. You hesitate, unsure.")
    update_stat("clarity", -5)
show_stats()

# Final Scene: The Sacred Temple
print("\n🏛️ At last, you arrive at the Sacred Temple. The gates open at your touch.")
print("You are greeted by shimmering beings who recognize your spirit.")
final_card = draw_tarot()
print(f"\n🃏 A final card awaits you... It is {final_card}.")
print("This card reflects what you’ve become through your journey.")

# Ending Evaluation
if data['alignment'] >= 80 and "Star Dust" in data['inventory']:
    print("\n✨ You have become a radiant guide. Others will follow the light you now carry.")
elif data['clarity'] >= 80 and "Moonstone" in data['inventory']:
    print("\n🌙 You are now a wise dreamer. You see what others cannot.")
elif data['energy'] <= 30:
    print("\n⛰️ You made it... but the trail has left you weary. Rest is your reward.")
else:
    print("\n🌌 You are still a seeker, but the Temple has awakened something in you. A new journey will begin.")

print("\n🪬 Thank you for walking The Tarot Trail.")