import React, { useState } from "react";

const Chatbot = () => {
    const [messages, setMessages] = useState([
        { from: "bot", text: "Hi! Ask me for an essay or a poem on any topic." }
    ]);
    const [input, setInput] = useState("");
    const [botType, setBotType] = useState("essay"); // "essay" or "poem"
    const [loading, setLoading] = useState(false);

    const handleSend = async () => {
        if (!input.trim()) return;
        setMessages(msgs => [...msgs, { from: "user", text: input }]);
        setLoading(true);

        // Decide endpoint based on botType
        const endpoint = botType === "essay" ? "/essay-direct" : "/poem-direct";

        try {
            // Construct URL with parameter 'topic' as per backend API
            const params = new URLSearchParams({ topic: input });
            const response = await fetch(`${endpoint}?${params}`);

            if (!response.ok) {
                throw new Error(`API Error: ${response.statusText}`);
            }

            const data = await response.json();
            setMessages(msgs => [...msgs, { from: "bot", text: data.result }]);
        } catch (err) {
            setMessages(msgs => [...msgs, { from: "bot", text: `Error: ${err.message}` }]);
        }
        setInput("");
        setLoading(false);
    };

    return (
        <div style={{ maxWidth: 500, margin: "auto", padding: 16 }}>
            <h2>Gemini Chatbot</h2>
            <div>
                {/* Tabs to select essay or poem generation */}
                <select value={botType} onChange={e => setBotType(e.target.value)} style={{ marginBottom: "1em" }}>
                    <option value="essay">Generate Essay</option>
                    <option value="poem">Generate Poem</option>
                </select>
            </div>
            <div style={{
                minHeight: 200, border: "1px solid #ccc", padding: 10, marginBottom: "1em", background: "#fafafa"
            }}>
                {messages.map((msg, idx) => (
                    <div key={idx} style={{ textAlign: msg.from === "user" ? "right" : "left" }}>
                        <b>{msg.from === "user" ? "You" : "Bot"}:</b> {msg.text}
                    </div>
                ))}
                {loading && <div>Bot is typing...</div>}
            </div>
            <input
                value={input}
                onChange={e => setInput(e.target.value)}
                onKeyDown={e => e.key === "Enter" ? handleSend() : null}
                style={{ width: "80%" }}
                placeholder={`Type your ${botType} topic...`}
                disabled={loading}
            />
            <button onClick={handleSend} disabled={loading || !input.trim()}>
                {botType === "essay" ? "Generate Essay" : "Generate Poem"}
            </button>
        </div>
    );
};

export default Chatbot;
